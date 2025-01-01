import apis.entities.methodologytrends.EntityMethodologyTrends as EntityMethodologyTrends

class ServicesMethodologyTrends():

    entity = None

    def __init__(self):

        self.entity = EntityMethodologyTrends.EntityMethodologyTrends()

    async def check_candles_entity(self,candles):

        return await self.entity.check_candles(candles)

    async def check_candles(self,candles):

        return await self.check_candles_entity(candles)
    
    async def check_rsi(self,rsi):

        return await self.entity.check_rsi(rsi)

