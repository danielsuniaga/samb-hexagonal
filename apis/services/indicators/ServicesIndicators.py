import apis.entities.indicators.EntityIndicators as EntityIndicators

class ServicesIndicators():

    entity = None

    def __init__(self):

        self.entity = EntityIndicators.EntityIndicators()

    def generate_rsi(self,candles):

        return self.entity.generate_rsi(candles)
    
    def generate_sma(self,candles,indicators): 

        return self.entity.generate_sma(candles,indicators)
    
    def get_sma_short(self):

        return self.entity.get_sma_short()
    
    def get_candles_last(self,candles):

        return self.entity.generate_candle_last(candles)