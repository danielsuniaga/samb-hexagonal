import apis.repositories.predictmodels.RepositoryPredictModels as RepositoryPredictModels
import apis.entities.predictmodels.EntityPredictModels as EntityPredictModels
class ServicesPredictModels:

    repository = None

    entity = None

    ServiceDates = None

    def __init__(self):
        self.repository = RepositoryPredictModels.RepositoryPredictModels()
        self.entity = EntityPredictModels.EntityPredictModels()

    def init_services_dates(self, value):
        self.ServiceDates = value
        return True

    def generate_id(self):
        return self.entity.generate_id()

    def init_data_samb_predict_models_data(self, data):
        return {
            'id': 'test',
            'dictionary': 'test',
            'registration_date': 'test',
            'update_date': 'test',
            'state': 'test'
        }
    
    def get_config_accuracy_min(self):
        return self.entity.get_config_accuracy_min()
    
    def get_config_probability_min(self):
        return self.entity.get_config_probability_min()
    
    def get_current_date_hour(self):
        if not self.ServiceDates:
            return False
        
        return self.ServiceDates.get_current_date_hour()
    
    def get_config_condition(self):
        return self.entity.get_config_condition()

    def init_samb_predict_models(self, data):
        # print("data: ",data)
        return {
            'id': self.generate_id(),
            'id_models': data['model_id'],
            'accuracy_min': self.get_config_accuracy_min(),
            'probability_min': self.get_config_probability_min(),
            'model_name': data['model_name'],
            'prediction': data['prediction'],
            'prediction_label': data['prediction_label'],
            'probability_loss': data['probability_loss'],
            'probability_win': data['probability_win'],
            'confidence': data['confidence'],
            'confidence_percentage': data['confidence_percentage'],
            'data_shape': data['data_shape'],
            'features_count': data['features_count'],
            'registration_date': self.get_current_date_hour(),
            'update_date': self.get_current_date_hour(),
            'state': self.get_config_condition()
        }

    def init_data_add(self,data):

        return {
            'samb_predict_models': self.init_samb_predict_models(data),
            'samb_predict_models_data': self.init_data_samb_predict_models_data(data)
        }
    
    def add_repository(self, data):

        # return True 
        return self.repository.add(data)

    def add(self,data):

        data_persistent = self.init_data_add(data)

        result = self.add_repository(data_persistent)

        print(f"Predict model added with ID: {result}")

        return result