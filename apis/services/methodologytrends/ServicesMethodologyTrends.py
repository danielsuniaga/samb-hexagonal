import apis.entities.methodologytrends.EntityMethodologyTrends as EntityMethodologyTrends

class ServicesMethodologyTrends():

    entity = None

    def __init__(self):

        self.entity = EntityMethodologyTrends.EntityMethodologyTrends()

    def check_candles_entity(self,candles):

        return self.entity.check_candles(candles)

    def check_candles(self,candles):

        return self.check_candles_entity(candles)
    
    def check_rsi(self,rsi):

        return self.entity.check_rsi(rsi)
    
    def check_sma(self,sma,last_candle):

        return self.entity.check_sma(sma,last_candle)
    
    def check_result_indicators(self,result_indicators):

        return self.entity.check_result_indicators(result_indicators)
    
    def check_monetary_filters(self,monetary_filter):

        return self.entity.check_monetary_filters(monetary_filter)

