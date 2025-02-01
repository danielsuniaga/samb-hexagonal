from decouple import config

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.preprocessing import StandardScaler

from sklearn.neural_network import MLPClassifier

import pickle

class EntityModels():

    config=None

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
            
            results[name] = {
            'id': self.config['id_models'][name],
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
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