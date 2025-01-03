import apis.entities.indicators.EntityIndicators as EntityIndicators

class ServicesIndicators():

    entity = None

    def __init__(self):

        self.entity = EntityIndicators.EntityIndicators()

    async def generate_rsi(self,candles):

        return await self.entity.generate_rsi(candles)
    
    async def generate_sma(self,candles,indicators): 

        return await self.entity.generate_sma(candles,indicators)
    
    def get_sma_short(self):

        return self.entity.get_sma_short()