from decouple import config

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report,confusion_matrix, ConfusionMatrixDisplay,precision_score,recall_score,f1_score
from sklearn.preprocessing import StandardScaler

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler

class EntityModels():

    config=None

    def __init__(self):
        
        self.init_config()

    def init_config(self):

        self.config = {
            'active':int(config("ACTIVE_GENERAL_ML_LOGISTIC_REGRESSION")),
            'id_models':
                {
                    'regression_logistic':config("ID_MODEL_REGRESSION_LOGISTIC"),
                    'decision_tree':config("ID_MODEL_DECISION_TREE"),
                    'random_forest':config("ID_MODEL_RANDOM_FOREST"),
                    'mlp':config("ID_MODEL_MLP")
                }
        }

    def get_config_active(self):
        
        return self.config['active']
    
    def init_data(self,data):

        y = data['entry_result']

        X = data.drop(columns=['entry_result'])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.09, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    def train_models(self, x, y):

        x_scaled = self.scale_data(x)
        
        model_regression_logistic = self.train_logistic_regression(x_scaled, y)

        model_decisiontree = self.train_decision_tree(x_scaled, y)

        model_random_forest = self.train_random_forest(x_scaled, y)

        model_mlp = self.train_mlp(x_scaled, y)

        return model_regression_logistic, model_decisiontree, model_random_forest, model_mlp

    def evaluate_models(self, models, X_test, y_test):
        
        X_test_scaled = self.scale_data(X_test)
        
        results = {}
        
        for name, model in models.items():

            y_pred = model.predict(X_test_scaled)

            accuracy = accuracy_score(y_test, y_pred)

            precision = precision_score(y_test, y_pred, average='weighted')

            recall = recall_score(y_test, y_pred, average='weighted')

            f1 = f1_score(y_test, y_pred, average='weighted')

            report = classification_report(y_test, y_pred)

            confusion = confusion_matrix(y_test, y_pred)
            
            results[name] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'classification_report': report,
            'confusion_matrix': confusion
            }
        
        return results

    def scale_data(self, x):

        scaler = StandardScaler()

        return scaler.fit_transform(x)

    def train_logistic_regression(self, x, y):

        model = LogisticRegression(max_iter=1000)

        model.fit(x, y)

        return model

    def train_decision_tree(self, x, y):

        model = DecisionTreeClassifier(max_depth=1, random_state=42)

        model.fit(x, y)

        return model

    def train_random_forest(self, x, y):

        model = RandomForestClassifier(n_estimators=5, random_state=42)

        model.fit(x, y)

        return model

    def train_mlp(self, x, y):

        model = MLPClassifier(hidden_layer_sizes=(50), max_iter=2000, random_state=42)

        model.fit(x, y)

        return model