import uuid

from decouple import config

class EntityFramework():

    config_add = None

    def __init__(self):

        self.init_config_add()

    def init_config_add(self):

        self.config_add = {
            'description':config("DESCRIPTION_FRAMEWORK"),
            'condition':config("CONDITION")
        }

    def get_config_add_description(self):

        return self.config_add['description']
    
    async def get_config_add_condition(self):

        return self.config_add['condition']

    def generate_id(self):
        
        return uuid.uuid4().hex