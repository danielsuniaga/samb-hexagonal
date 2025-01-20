import uuid

from decouple import config

class EntityEntrysResults:

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
    
    def get_data_results_entrys_add_persistence_loss(self,data):

        return data['loss']
    
    def get_data_results_entrys_add_persistence_profit(self,data):

        return data['profit']

    
    def get_data_result_entry_add_persistence(self,data):

        if not data['status']:

            return self.get_data_results_entrys_add_persistence_loss(data)

        return self.get_data_results_entrys_add_persistence_profit(data)