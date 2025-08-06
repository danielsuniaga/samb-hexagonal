from decouple import config

import uuid

class EntityPredictModels: 

    config = None

    def __init__(self):
        self.init_config()

    def init_config(self):
        self.config = {
            'condition': '1',
            'accuracy_min': float(config("ML_ACCURACY_MIN")),
            'probability_min': float(config("PROBABILITY_MIN")),
            'id_predict_models':None
        }
        return True
    
    def set_config(self, key, value):
        if not self.config:
            self.init_config()
        self.config[key] = value
        return True
    
    def set_config_id_predict_models(self, id_predict_models):
        self.set_config('id_predict_models', id_predict_models)
        return True
    
    def get_config(self, key):
        if not self.config:
            self.init_config()
        return self.config[key]
    
    def get_config_id_predict_models(self):
        return self.get_config('id_predict_models')
    
    def get_config_condition(self):
        return self.get_config('condition')
    
    def get_config_accuracy_min(self):
        return self.get_config('accuracy_min')
    
    def get_config_probability_min(self):
        return self.get_config('probability_min')

    def generate_id(self):
        return uuid.uuid4().hex