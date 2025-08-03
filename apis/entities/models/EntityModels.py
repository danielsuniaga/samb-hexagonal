from decouple import config

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler

from sklearn.neural_network import MLPClassifier

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler, Normalizer

import pickle
import numpy as np
import pandas as pd

class EntityModels():

    config=None
    scaler=None
    feature_names=None  # Guardar feature_names como atributo de la clase

    def __init__(self):
        
        self.init_config()

    def init_config(self):

        self.config = {
            'active':int(config("ACTIVE_GENERAL_ML")),
            'directory_general':config("DIRECTORY_ML_GENERAL"),
            'name_project':config("PROJECT_NAME"),
            'accuracy_min': float(config("ML_ACCURACY_MIN")),
            'probability_min': float(config("PROBABILITY_MIN")),
            'best_model': None,
            'result_models': None,
            'id_models':
                {
                    'regression_logistic':config("ID_REGRESSION_LOGISTIC"),
                    'decision_tree':config("ID_DECISION_TREE"),
                    'random_forest':config("ID_RANDOM_FOREST"),
                    'mlp':config("ID_MLP")
                },
            'name_models':
                {
                    'regression_logistic':config("NAME_REGRESSION_LOGISTIC"),
                    'decision_tree':config("NAME_DECISION_TREE"),
                    'random_forest':config("NAME_RANDOM_FOREST"),
                    'mlp':config("NAME_MLP")
                },
            'scaler':
                {
                    'name':config("NAME_SCALER"),
                }
        }

        return True
    
    def get_config_scaler_name(self):
        return self.config['scaler']['name']
    
    def get_config_probability_min(self):
        return self.config['probability_min']
    
    def get_name_models_by_id_models(self, id_model):
        for name, id_value in self.config['id_models'].items():
            if id_value == id_model:
                return self.config['name_models'][name]
        
        return None
    
    def set_config(self, key, value):

        if key in self.config:
            self.config[key] = value
            return True
        return False
    
    def set_config_accuracy_min(self, value):

        return self.set_config('accuracy_min', value)
    
    def set_config_result_models(self, value):

        return self.set_config('result_models', value)
    
    def get_config_accuracy_min(self):
        
        return self.config['accuracy_min']
    
    def get_config_best_model(self):

        return self.config['best_model']
    
    def get_config_name_project(self):
        
        return self.config['name_project']
    
    def get_config_directory_general(self):
        
        return self.config['directory_general']

    def get_config_active(self):
        
        return self.config['active']

    def clean_nan_data(self, X, y):

        filas_originales = len(X)
        
        # Si es pandas DataFrame
        if hasattr(X, 'isna'):
            # Eliminar filas con cualquier valor NaN o infinito
            mask_limpio = ~(X.isna().any(axis=1) | X.isin([np.inf, -np.inf]).any(axis=1))
            X = X[mask_limpio]
            y = y[mask_limpio]
        else:
            # Si es numpy array
            # Eliminar filas con NaN o infinitos
            mask_limpio = ~(np.isnan(X).any(axis=1) | np.isinf(X).any(axis=1))
            X = X[mask_limpio]
            y = y[mask_limpio]
        
        filas_finales = len(X)
        filas_eliminadas = filas_originales - filas_finales

        return X, y
    
    def init_data(self, data):
        """
        Inicializa los datos para entrenamiento y test, delegando responsabilidades.
        """
        y = self.extract_target(data)
        X = self.extract_features(data)
        X, y = self.clean_nan_data(X, y)
        X_train, X_test, y_train, y_test = self.split_data(X, y)
        self.scaler = self.create_and_save_scaler(X_train)
        X_train_scaled, X_test_scaled = self.apply_scaler(X_train, X_test)
        return X_train_scaled, X_test_scaled, y_train, y_test

    def extract_target(self, data):
        """
        Extrae la variable objetivo (y) del DataFrame.
        """
        return data['entry_result']

    def extract_features(self, data):
        """
        Extrae las variables predictoras (X) del DataFrame.
        """
        return data.drop(columns=['entry_result', 'year', 'day', 'hour', 'month'])

    def split_data(self, X, y):
        """
        Divide los datos en conjuntos de entrenamiento y prueba.
        """
        return train_test_split(
            X, y,
            test_size=0.12,
            stratify=y,
            random_state=2024,
            shuffle=True
        )

    def create_and_save_scaler(self, X_train):
        """
        Crea y guarda el scaler entrenado con los datos de entrenamiento.
        """
        scaler = StandardScaler()
        scaler.fit(X_train)
        scaler_path = self.get_config_directory_general() + self.get_config_scaler_name()
        try:
            with open(scaler_path, 'wb') as scaler_file:
                pickle.dump(scaler, scaler_file)
        except Exception as e:
            print(f"❌ Error al guardar el scaler: {str(e)}")
        return scaler

    def apply_scaler(self, X_train, X_test):
        """
        Aplica el scaler a los conjuntos de entrenamiento y prueba.
        """
        X_train_scaled = self.scaler.transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled
    
    def train_models(self, x, y):

        # Los datos ya vienen escalados de init_data
        model_regression_logistic = self.train_logistic_regression(x, y)
        

        model_decisiontree = self.train_decision_tree(x, y)

        model_random_forest = self.train_random_forest(x, y)

        model_mlp = self.train_mlp(x, y)

        return model_regression_logistic, model_decisiontree, model_random_forest, model_mlp

    def evaluate_models(self, models, X_test, y_test):
        
        # Los datos ya vienen escalados de init_data
        results = {}
        
        for name, model in models.items():

            y_pred = model.predict(X_test)
            
            # Probabilidades para métricas avanzadas
            y_proba = None
            if hasattr(model, 'predict_proba'):
                y_proba = model.predict_proba(X_test)[:, 1]  # Probabilidad de clase positiva

            # Métricas básicas
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')
            
            # Métricas específicas para trading
            auc_score = None
            if y_proba is not None:
                try:
                    auc_score = roc_auc_score(y_test, y_proba)
                except:
                    auc_score = None
            
            # Matriz de confusión para métricas detalladas
            cm = confusion_matrix(y_test, y_pred)
            tn, fp, fn, tp = cm.ravel() if cm.size == 4 else (0, 0, 0, 0)
            
            # Métricas específicas de trading
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0  # True Negative Rate
            sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0  # True Positive Rate (recall)
            
            # Precision y Recall específicos para cada clase
            precision_win = tp / (tp + fp) if (tp + fp) > 0 else 0  # Precisión para predicciones ganadoras
            precision_loss = tn / (tn + fn) if (tn + fn) > 0 else 0  # Precisión para predicciones perdedoras
            
            # Balanced Accuracy (mejor para clases desbalanceadas)
            balanced_acc = (sensitivity + specificity) / 2
            
            # Win Rate vs Predicted Win Rate
            actual_win_rate = sum(y_test) / len(y_test)
            predicted_wins = sum(y_pred)
            predicted_win_rate = predicted_wins / len(y_pred) if len(y_pred) > 0 else 0
            
            results[name] = {
                'id': self.config['id_models'][name],
                # Métricas básicas
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                # Métricas avanzadas
                'auc_score': auc_score,
                'balanced_accuracy': balanced_acc,
                'specificity': specificity,
                'sensitivity': sensitivity,
                # Métricas de trading específicas
                'precision_win': precision_win,
                'precision_loss': precision_loss,
                'actual_win_rate': actual_win_rate,
                'predicted_win_rate': predicted_win_rate,
                # Conteos de la matriz de confusión
                'true_positives': int(tp),
                'true_negatives': int(tn),
                'false_positives': int(fp),
                'false_negatives': int(fn),
                # Métricas derivadas
                'total_predictions': len(y_pred),
                'win_predictions': int(predicted_wins)
            }
        
        return results

    def scale_data(self, x):

        scaler = StandardScaler()

        return scaler.fit_transform(x)

    def train_logistic_regression(self, x, y):

        # Hiperparámetros ajustados para 120+ features de las 30 velas OHLC
        model = LogisticRegression(
            max_iter=10000,          # MUCHAS más iteraciones para 120+ features
            C=1.0,                   # Regularización moderada (era 10.0)
            solver='lbfgs',          # Mejor solver para muchas features
            random_state=42,         # Reproducibilidad
            class_weight='balanced', # Maneja desbalance de clases automáticamente
            penalty='l2',            # Solo L2 (lbfgs no soporta elasticnet)
            tol=1e-6                 # Tolerancia más estricta para convergencia
        )

        model.fit(x, y)

        return model
    
    def analyze_feature_importance(self, model, feature_names):
        """
        Analiza la importancia de las características en el modelo de regresión logística
        """
        if hasattr(model, 'coef_'):
            # Obtener los coeficientes (importancia de las variables)
            coefficients = model.coef_[0]
            
            # Crear un diccionario con nombres de variables y sus coeficientes
            feature_importance = {}
            for i, coef in enumerate(coefficients):
                if i < len(feature_names):
                    feature_importance[feature_names[i]] = abs(coef)  # Valor absoluto
            
            # Ordenar por importancia (mayor a menor)
            sorted_features = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
            
            print("\n🔍 IMPORTANCIA DE VARIABLES (Regresión Logística):")
            print("=" * 50)
            for i, (feature, importance) in enumerate(sorted_features[:10]):  # Top 10
                print(f"{i+1:2d}. {feature:25s}: {importance:.4f}")
            
            # Mostrar variables eliminadas (coeficiente = 0)
            zero_coef = [name for name, importance in feature_importance.items() if importance == 0]
            if zero_coef:
                print(f"\n❌ Variables eliminadas por L1: {len(zero_coef)}")
                
            return sorted_features
        
        return None

    def train_decision_tree(self, x, y):

        # Decision Tree menos restrictivo
        model = DecisionTreeClassifier(
            max_depth=8,                    # Mucho más profundo (era 1)
            min_samples_leaf=1,             # Menos restrictivo
            class_weight='balanced',        # Manejo de desbalance
            criterion='gini',               # Criterio de división
            splitter='best',                # Mejor división
            random_state=42                 # Reproducibilidad
        )

        model.fit(x, y)

        return model

    def train_random_forest(self, x, y):

        # Random Forest EXTREMADAMENTE optimizado para superar 0.6
        model = RandomForestClassifier(
            n_estimators=1000,              # MUCHOS más árboles (era 500)
            max_depth=None,                 # Sin límite de profundidad (era 25)
            min_samples_split=2,            # Mínimo permitido (era 1 - INVÁLIDO)
            min_samples_leaf=1,             # Máxima flexibilidad
            max_features='sqrt',            # Volver a 'sqrt' (mejor que log2)
            class_weight='balanced_subsample', # Balanceo por subsample
            bootstrap=True,                 # Usar bootstrap
            oob_score=True,                 # Out-of-bag score
            n_jobs=-1,                      # Usar todos los cores
            random_state=42,                # Reproducibilidad
            criterion='gini',               # Volver a 'gini' (más estable)
            max_samples=1.0,                # 100% de muestras por árbol
            warm_start=False,               # No usar warm start
            ccp_alpha=0.0,                  # Sin poda de complejidad
            max_leaf_nodes=None             # Sin límite de hojas
        )

        model.fit(x, y)

        return model

    def train_mlp(self, x, y):

        # MLP optimizado para mejor performance
        model = MLPClassifier(
            hidden_layer_sizes=(100, 50, 25),  # 3 capas (era solo 50)
            max_iter=5000,                     # Más iteraciones (era 2000)
            alpha=0.0001,                      # Menos regularización (default 0.0001)
            learning_rate='adaptive',          # Ajuste adaptativo del learning rate
            learning_rate_init=0.001,          # Learning rate inicial
            solver='adam',                     # Optimizador Adam (mejor que default)
            activation='relu',                 # Función de activación ReLU
            early_stopping=True,               # Parar si no mejora
            validation_fraction=0.1,           # 10% para validación
            n_iter_no_change=50,              # Paciencia para early stopping
            random_state=42,                   # Reproducibilidad
            batch_size='auto'                  # Batch size automático
        )

        model.fit(x, y)

        return model
    
    def  add_models_directory(self, data):

        for name, model in data.items():

            path = self.get_config_directory_general()+self.config['name_models'][name]

            try:

                with open(path, 'wb') as model_file:

                    pickle.dump(model, model_file)

            except Exception as e:

                return False

        return True
    

    def get_head_message_reports(self):

        return f"DAILY REPORTS ML ({self.get_config_name_project()})\n"
    
    def generate_message_reports(self, results):

        message = self.get_head_message_reports()
        
        for model_name, metrics in results.items():

            message += f"{model_name.upper()}: "
            message += f"Accuracy({metrics['accuracy']:.3f}), "
            message += f"Precision({metrics['precision']:.3f}), "
            message += f"Recall({metrics['recall']:.3f}), "
            message += f"F1 Score({metrics['f1_score']:.3f})\n"
        
        return message
    
    def open_model(self, path): 
        try:
            with open(path, 'rb') as model_file:
                loaded_model = pickle.load(model_file)
                if loaded_model is None:
                    return {'status': False, 'message': 'Failed to load model'}
                return {'status': True, 'model': loaded_model, 'path': path}
        except FileNotFoundError:
            return {'status': False, 'message': f'Model file not found: {path}'}
        except Exception as e:
            return {'status': False, 'message': f'Error loading model: {str(e)}'}
    
    def open_scaler(self, path):
        """
        Cargar el scaler guardado desde un archivo pickle
        """
        try:
            with open(path, 'rb') as scaler_file:
                loaded_scaler = pickle.load(scaler_file)
                if loaded_scaler is None:
                    return {'status': False, 'message': 'Failed to load scaler'}
                return {'status': True, 'scaler': loaded_scaler, 'path': path}
        except FileNotFoundError:
            return {'status': False, 'message': f'Scaler file not found: {path}'}
        except Exception as e:
            return {'status': False, 'message': f'Error loading scaler: {str(e)}'}
        
    def init_data_get_predict_model(self,data):

        candles = data.get('candles', [])

        # Extraer las 30 últimas velas (o las primeras 30 si es necesario)
        candle_list = candles.get('candles', [])
        if len(candle_list) < 30:
            raise ValueError("No hay suficientes velas en el parámetro 'candles' (se requieren al menos 30)")

        # Tomar las últimas 30 velas (asumiendo que están ordenadas de más antigua a más reciente)
        last_30_candles = candle_list[-30:]

        # Construir el diccionario de datos reemplazando los campos 'test' por los valores reales de las velas
        data = {
            'description_methodology': data['description_methodology'],
            'entry_type': data['entry_type'],
            'entry_condition': data['entry_condition'],
            'entry_amount': data['entry_amount'],
            'sma_30_value': data['sma_30_value'],
            'sma_10_value': data['sma_10_value'],
            'rsi_value': data['rsi_value'],
        }

        # Agregar los campos de las 30 velas
        for idx, candle in enumerate(last_30_candles, start=1):
            data[f'candle_{idx}_open'] = candle.get('open')
            data[f'candle_{idx}_high'] = candle.get('high')
            data[f'candle_{idx}_low'] = candle.get('low')
            data[f'candle_{idx}_close'] = candle.get('close')
        return data

    def load_model_and_scaler(self, id_models):
        """
        Carga el modelo y scaler específicos por ID.
        Responsabilidad: Gestión de carga de archivos ML.
        """
        name_models = self.get_name_models_by_id_models(id_models)
        if not name_models:
            return {'status': False, 'message': f'Model ID {id_models} not found'}

        # Cargar modelo
        model_path = self.get_config_directory_general() + name_models
        model_result = self.open_model(model_path)
        if not model_result['status']:
            return {'status': False, 'message': 'Failed to load model'}

        # Cargar scaler
        scaler_path = self.get_config_directory_general() + "scaler.pkl"
        scaler_result = self.open_scaler(scaler_path)
        if not scaler_result['status']:
            return {'status': False, 'message': scaler_result['message']}
        
        return {
            'status': True,
            'model': model_result['model'],
            'model_name': name_models,
            'scaler': scaler_result['scaler']
        }

    def prepare_prediction_data(self, data, scaler):
        """
        Prepara y escala los datos para predicción.
        Responsabilidad: Transformación de datos de entrada.
        """
        # Preparar datos con las 30 velas reales
        data_models = self.init_data_get_predict_model(data)
        
        # Convertir a DataFrame y aplicar scaler
        data_df = pd.DataFrame([data_models])
        data_scaled = scaler.transform(data_df)
        
        return data_scaled

    def calculate_probabilities(self, model, data_scaled):
        """
        Calcula las probabilidades y confianza del modelo.
        Responsabilidad: Cálculo de métricas de predicción.
        """
        probabilities = None
        probability_loss = 0.0
        probability_win = 0.0
        confidence = 0.0
        
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(data_scaled)
            probability_loss = float(probabilities[0][0])  # Probabilidad de pérdida (clase 0)
            probability_win = float(probabilities[0][1])   # Probabilidad de ganancia (clase 1)
            confidence = float(max(probabilities[0]))      # Confianza (mayor probabilidad)
        
        return probability_loss, probability_win, confidence

    def format_prediction_result(self, id_models, model_name, prediction_result, 
                                probability_loss, probability_win, confidence, data_scaled):
        """
        Formatea el resultado final de la predicción.
        Responsabilidad: Estructuración de respuesta.
        """
        return {
            'status': True,
            'model_id': id_models,
            'model_name': model_name,
            'prediction': prediction_result,           # 0 o 1
            'prediction_label': 'GANANCIA' if prediction_result == 1 else 'PÉRDIDA',
            'probability_loss': probability_loss,      # Probabilidad de pérdida [0-1]
            'probability_win': probability_win,        # Probabilidad de ganancia [0-1]
            'confidence': confidence,                  # Confianza del modelo [0-1]
            'confidence_percentage': confidence * 100, # Confianza en porcentaje
            'data_shape': data_scaled.shape,           # Para debug
            'features_count': data_scaled.shape[1]     # Número de características
        }

    def get_predict_models(self, id_models, data):
        """
        Método principal para obtener predicciones del modelo.
        Responsabilidad: Orquestación del proceso de predicción.
        """
        # 1. Cargar modelo y scaler
        load_result = self.load_model_and_scaler(id_models)
        if not load_result['status']:
            return load_result
        
        model = load_result['model']
        model_name = load_result['model_name'] 
        scaler = load_result['scaler']
        
        # Asignar scaler al atributo de clase (para compatibilidad)
        self.scaler = scaler

        # 2. Preparar datos
        data_scaled = self.prepare_prediction_data(data, scaler)
        
        # 3. Realizar predicción
        prediction = model.predict(data_scaled)
        prediction_result = int(prediction[0])  # 0 = pérdida, 1 = ganancia
        
        # 4. Calcular probabilidades
        probability_loss, probability_win, confidence = self.calculate_probabilities(model, data_scaled)
        
        # 5. Formatear resultado
        return self.format_prediction_result(
            id_models, model_name, prediction_result,
            probability_loss, probability_win, confidence, data_scaled
        )

    def check_predict_models(self, data):

        if data['probability_win'] < self.get_config_probability_min():
            
            return {'status': False, 'message': f"Probability {data['probability_win']} is below the minimum required {self.get_config_probability_min()}"}

        return {'status': True, 'message': 'Probability is acceptable.'}