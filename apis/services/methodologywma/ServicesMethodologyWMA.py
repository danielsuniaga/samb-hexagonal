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
    
    def check_rsi(self,rsi):
            
        return self.entity.check_rsi(rsi)
    
    def check_sma(self,sma,last_candle):

        return self.entity.check_sma(sma,last_candle)
    
    def check_result_indicators(self,result_indicators):
        
        return self.entity.check_result_indicators(result_indicators)
    
    def check_monetary_filters(self,monetary_filter):
        
        return self.entity.check_monetary_filters(monetary_filter)
    
    def get_type_entry_positions(self):

        return self.entity.get_type_entry_positions()
    
    def get_candle_removed(self):

        return self.entity.get_candle_removed()
    
    def get_condition_entry(self):
        
        return self.entity.get_condition_entry()
    
    def set_result_entrys(self,result):

        return self.entity.set_result_entrys_result(result)
    
    def set_result_candles(self,result):

        return self.entity.set_result_entrys_candles(result)
    
    def get_result_entrys_result(self):

        return self.entity.get_result_entrys_result()
    
    def get_name(self):

        return self.entity.get_name()
