from decouple import config

import uuid

class EntityReports():

    condition = None

    def __init__(self):

        self.init_condition()

    def init_condition(self):

        self.condition = config("CONDITION")

        return True
    
    def get_condition(self):

        return self.condition

    def generate_id(self):
        
        return uuid.uuid4().hex