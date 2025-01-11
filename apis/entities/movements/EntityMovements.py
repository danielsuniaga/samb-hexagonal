import uuid

from decouple import config

class EntityMovements():

    candles = None

    condition = None

    def __init__(self):

        self.init_condition()
        
    def init_condition(self):
        
        self.condition = config("CONDITION")

        return True
    
    def get_condition(self):
        
        return self.condition   

    def set_candles(self,candles):
        
        self.candles = candles

        return True 
    
    def get_candles(self):
        
        return self.candles
    
    def generate_id(self):

        return uuid.uuid4().hex