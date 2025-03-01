from decouple import config

class EntityMethodologys:

    config = None

    def __init__(self):

        self.init_config()

    def init_config(self):

        self.config = {
            'condition_success': config('CONDITION_SUCCESS'),
        }

        return True
    
    def get_config(self,key):

        return self.config[key]
    
    def get_config_condition_success(self):

        return self.get_config('condition_success')
    