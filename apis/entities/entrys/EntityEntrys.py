import uuid

from decouple import config

class EntityEntrys():

    condition = None

    data = None

    project_name = None

    def __init__(self):

        self.init_condition()

        self.init_project_name()

    def init_project_name(self):

        self.project_name = config("PROJECT_NAME")

        return True
    
    def get_project_name(self):

        return self.project_name

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