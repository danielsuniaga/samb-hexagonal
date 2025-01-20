import uuid

from decouple import config

class EntityEntrys():

    condition = None

    data = None

    def __init__(self):

        self.init_condition()

    def set_data(self,data):

        self.data = data

        return True
    
    def get_data(self):

        return self.data    

    def init_condition(self):

        self.condition = config("CONDITION")

        return True
    
    def get_condition(self):
        
        return self.condition

    def generate_id(self):

        return uuid.uuid4().hex