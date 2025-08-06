import uuid

class EntityEntrysPredictModels:

    config = None

    def __init__(self):
        self.init_config()

    def init_config(self):
        self.config = {
            'condition': '1'
        }
        return True
    
    def get_config(self, key):
        if not self.config:
            self.init_config()
        return self.config[key]
    
    def get_config_condition(self):
        return self.get_config('condition')

    def generate_id(self):
        return uuid.uuid4().hex