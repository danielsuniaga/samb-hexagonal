import apis.entities.methodologywma.EntityMethodologyWMA as EntityMethodologyWMA

class ServicesMethodologyWMA:

    entity = None

    def __init__(self):

        self.entity = EntityMethodologyWMA.EntityMethodologyWMA()

    def get_id(self):
        
        return self.entity.get_id()
    
    def generate_candles(self,candles):
        
        return self.entity.generate_candles(candles)
    
    def set_indicators(self,indicators):
        
        return self.entity.set_indicators(indicators)
    
    def get_indicators(self):

        return self.entity.get_indicators()
    
    def check_candles(self):
        
        return self.entity.check_candles()