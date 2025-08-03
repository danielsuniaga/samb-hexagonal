import apis.repositories.predictmodels.RepositoryPredictModels as RepositoryPredictModels

class ServicesPredictModels:

    repository = None

    def __init__(self):
        self.repository = RepositoryPredictModels.RepositoryPredictModels()

    def init_data_samb_predict_models_data(self, data):
        return {
            'id': 'test',
            'dictionary': 'test',
            'registration_date': 'test',
            'update_date': 'test',
            'state': 'test'
        }

    def init_samb_predict_models(self, data):
        return {
            'id': 'test',
            'id_models': 'test',
            'id_cronjobs': 'test',
            'accuracy_min': 'test',
            'probability_min': 'test',
            'model_name': 'test',
            'prediction': 'test',
            'prediction_label': 'test',
            'probability_loss': 'test',
            'probability_win': 'test',
            'confidence': 'test',
            'confidence_percentage': 'test',
            'data_shape': 'test',
            'features_count': 'test',
            'registration_date': 'test',
            'udpate_date': 'test',
            'state': 'test'
        }

    def init_data_add(self,data):

        return {
            'samb_predict_models': self.init_samb_predict_models(data),
            'samb_predict_models_data': self.init_data_samb_predict_models_data(data)
        }
    
    def add_repository(self, data):
        return self.repository.add(data)

    def add(self,data):

        data_persistent = self.init_data_add(data)

        result = self.add_repository(data_persistent)

        print(f"Predict model added with ID: {result}")

        return result