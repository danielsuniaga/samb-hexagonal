import apis.entities.models.EntityModels as EntityModels

class ServicesModels(): 

    entity = None

    ServicesDatasets = None

    def __init__(self):
        
        self.entity = EntityModels.EntityModels()
    
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
            'model_regression_logistic':model_regression_logistic,
            'model_decision_tree':model_decision_tree,
            'model_random_forest':model_random_forest,
            'model_mlp':model_mlp
        }
    
    def evaluate_models(self,models,X_test,y_test):

        return self.entity.evaluate_models(models,X_test,y_test)
    
    def generate_training_model(self):

        data = self.get_dataset()

        X_train, X_test, y_train, y_test = self.init_data(data)

        models = self.init_models(X_train, y_train)

        results = self.evaluate_models(models, X_test, y_test)
        
        return results