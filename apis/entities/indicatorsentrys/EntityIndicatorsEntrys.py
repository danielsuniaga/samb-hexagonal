import uuid

from decouple import config

class EntityIndicatorsEntrys:

    condition = None

    ids_indicators = None

    def __init__(self):

        self.init_condition() 

        self.init_ids_indicators() 

    def init_ids_indicators(self):

        self.ids_indicators = {
            'rsi10':config("RSI10"),
            'sma10':config("SMA10"),
            'sma30':config("SMA30")
        } 

        return True
    
    def get_ids_indicators_rsi10(self):

        return self.ids_indicators['rsi10']
    
    def get_ids_indicators_sma10(self): 

        return self.ids_indicators['sma10']
    
    def get_ids_indicators_sma30(self):

        return self.ids_indicators['sma30']

    def get_condition(self):
        
        return self.condition

    def init_condition(self):

        self.condition = config("CONDITION")

        return True  

    def generate_id(self):

        return uuid.uuid4().hex