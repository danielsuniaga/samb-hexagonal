import apis.entities.indicators.EntityIndicators as EntityIndicators

class ServicesIndicators():

    entity = None

    def __init__(self):

        self.entity = EntityIndicators.EntityIndicators()

    async def generate_rsi(self,candles):

        return await self.entity.generate_rsi(candles)