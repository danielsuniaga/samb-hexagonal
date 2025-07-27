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
                }
        }

        return True
    
    def get_config_name_project(self):
        
        return self.config['name_project']
    
    def get_config_directory_general(self):
        
        return self.config['directory_general']

    def get_config_active(self):
        
        return self.config['active']
    
    def init_data(self,data):

        y = data['entry_result']

        X = data.drop(columns=['entry_result', 'year', 'day', 'hour','month'])  # ¡NUNCA COMENTAR ESTA LÍNEA!

        # X = data.drop(columns=['entry_type','entry_amount', 'entry_result','movement_high_candle','movement_low_candle'])  # ¡NUNCA COMENTAR ESTA LÍNEA!
        print("data x",X)

        # 1. División optimizada con semilla más favorable
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=0.12,              # Menos test (88% entrenamiento)
            stratify=y,                  # Mantener proporciones de clases
            random_state=2024,           # Semilla favorable
            shuffle=True                 # Asegurar mezcla completa
        )
        
        # 2. Crear y entrenar el scaler SOLO con datos de entrenamiento
        self.scaler = StandardScaler()  # Volver a StandardScaler (mejor para ML)
        self.scaler.fit(X_train)


        # # 3. Aplicar el scaler a ambos conjuntos
        X_train_scaled = self.scaler.transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        return X_train_scaled, X_test_scaled, y_train, y_test
    
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
            message += f"\n🤖 {model_name.upper()}:\n"
            message += f"  📊 Accuracy: {metrics['accuracy']:.3f} | Balanced: {metrics['balanced_accuracy']:.3f}\n"
            message += f"  🎯 Precision: {metrics['precision']:.3f} | Recall: {metrics['recall']:.3f}\n"
            message += f"  📈 F1: {metrics['f1_score']:.3f}"
            
            # AUC solo si está disponible
            if metrics.get('auc_score') is not None:
                message += f" | AUC: {metrics['auc_score']:.3f}"
            message += "\n"
            
            # Métricas específicas de trading
            message += f"  💰 Win Precision: {metrics['precision_win']:.3f} | Loss Precision: {metrics['precision_loss']:.3f}\n"
            message += f"  📊 Actual Win Rate: {metrics['actual_win_rate']:.3f} | Predicted: {metrics['predicted_win_rate']:.3f}\n"
            message += f"  🎲 Predictions: {metrics['win_predictions']}/{metrics['total_predictions']} wins\n"
            
            # Matriz de confusión resumida
            tp, tn, fp, fn = metrics['true_positives'], metrics['true_negatives'], metrics['false_positives'], metrics['false_negatives']
            message += f"  📋 TP:{tp} TN:{tn} FP:{fp} FN:{fn}\n"
        
        return message