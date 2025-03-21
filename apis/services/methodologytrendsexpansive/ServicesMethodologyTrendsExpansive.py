import apis.entities.methodologytrendsexpansive.EntityMethodologyTrendsExpansive as EntityMethodologyTrendsExpansive

class ServicesMethodologyTrendsExpansive():

    entity = None

    def __init__(self):

        self.entity = EntityMethodologyTrendsExpansive.EntityMethodologyTrendsExpansive()

        self.entity.init_config()

    def get_id(self):
        
        return self.entity.get_id()
    
    def check_candles_entity(self,candles):

        return self.entity.check_candles(candles)
    
    def check_candles(self,candles):

        return self.check_candles_entity(candles)
    
    def check_rsi(self,rsi):

        return self.entity.check_rsi(rsi)
    
    def check_sma(self,sma,last_candle):

        return self.entity.check_sma(sma,last_candle)
    
    def add_indicator(self,indicators):

        return self.entity.add_indicators(indicators)
    
    def check_result_indicators(self,result_indicators):

        return self.entity.check_result_indicators(result_indicators)