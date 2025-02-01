from decouple import config

import uuid

class EntityMetricsEvaluationsModels():

    config = None

    def __init__(self):

        self.init_config()

    def init_config(self):

        self.config = {
            'condition': config("CONDITION"),
        }

        return True
    
    def get_config_condition(self):

        return self.config['condition']

    def generate_id(self):

        return uuid.uuid4().hex