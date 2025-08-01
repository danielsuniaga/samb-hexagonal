import apis.entities.models.EntityModels as EntityModels
import apis.repositories.models.RepositoryModels as RepositoryModels

class ServicesModels(): 

    entity = None

    repository = None

    ServicesDatasets = None

    def __init__(self):
        
        self.entity = EntityModels.EntityModels()
        self.repository = RepositoryModels.RepositoryModels()
    
    def init_services_datasets(self,value):

        self.ServicesDatasets = value

        return True

    def get_config_active(self):
        
        return self.entity.get_config_active()

    def get_active_model(self):

        if not self.get_config_active():
            
            return False
        
        return True
    
    def get_dataset(self):

        return self.ServicesDatasets.get_dataset()
    
    def init_data(self,data):

        return self.entity.init_data(data)
    
    def train_models(self,x,y):
        
        return self.entity.train_models(x,y)
    
    def init_models(self,x,y):

        model_regression_logistic,model_decision_tree,model_random_forest,model_mlp = self.train_models(x,y)

        return {
            'regression_logistic':model_regression_logistic,
            'decision_tree':model_decision_tree,
            'random_forest':model_random_forest,
            'mlp':model_mlp
        }
    
    def evaluate_models(self,models,X_test,y_test):

        return self.entity.evaluate_models(models,X_test,y_test)
    
    def add_models_directory(self, data):

        return self.entity.add_models_directory(data)
    
    def generate_training_model(self):

        data = self.get_dataset()

        X_train, X_test, y_train, y_test = self.init_data(data)

        models = self.init_models(X_train, y_train)

        self.add_models_directory(models)

        results = self.evaluate_models(models, X_test, y_test)
        
        return results
    
    def generate_message_reports(self,results):

        return self.entity.generate_message_reports(results)
    
    def get_directory_general(self):

        return self.entity.get_config_directory_general()
    
    def get_best_model_repository(self):

        return self.repository.get_best_model()
    
    def init_result_get_best_model(self, result):

        return result['data'][0]

    def get_best_model(self):

        result = self.get_best_model_repository()

        return self.init_result_get_best_model(result)
    
    def get_config_accuracy_min(self):  
        return self.entity.get_config_accuracy_min()
    
    def set_config_accuracy_min(self, value):

        return self.entity.set_config_accuracy_min(value)

    def check_models(self):

        result = self.get_best_model()

        if float(result['accuracy']) < float(self.get_config_accuracy_min()):

            return {'status': False, 'message': f"Accuracy {result['accuracy']} is below the minimum required {str(self.get_config_accuracy_min())}"}
        
        self.set_config_accuracy_min(result)

        return {'status': True, 'message': 'Models are checked successfully.'} 
    
    def get_config_best_model(self):

        return self.entity.get_config_best_model()
    
    def get_name_models_by_id_models(self, id_model):

        return self.entity.get_name_models_by_id_models(id_model)
    
    def get_predict_models(self,id_models):

        return self.entity.get_predict_models(id_models)
    
    def check_predict_models(self):

        best_model_info = self.get_best_model()

        result = self.get_predict_models(best_model_info['id'])

        return True