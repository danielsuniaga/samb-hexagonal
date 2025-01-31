from decouple import config

class EntityModels():

    config=None

    def __init__(self):
        
        self.init_config()

    def init_config(self):

        self.config = {
            'active':int(config("ACTIVE_GENERAL_ML_LOGISTIC_REGRESSION"))
        }

    def get_config_active(self):
        
        return self.config['active']