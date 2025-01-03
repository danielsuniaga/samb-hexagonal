from decouple import config

from decimal import Decimal

class EntityMethodologyTrends():

    candle_removed = None

    type_entry = None

    metrics_rsi = None

    def __init__(self):

        self.init_candle_removed()

        self.init_type_entry()

        self.init_metrics_rsi()

    def init_metrics_rsi(self):

        self.metrics_rsi = {
            'min':int(config("RSI_MIN")),
            'max':int(config("RSI_MAX")),
            'active':int(config("ACTIVE_RSI"))
        }

        return True
    
    def get_metrics_rsi_min(self):

        return self.metrics_rsi['min']
    
    def get_metrics_rsi_max(self):

        return self.metrics_rsi['max']

    def init_type_entry(self):

        self.type_entry = {
            'short':config("TYPE_ENTRY_SHORT"),
            'long':config("TYPE_ENTRY_LONG")
        }

        return True
    
    def get_type_entry_short(self):

        return self.type_entry['short']
    
    def get_type_entry_long(self):

        return self.type_entry['long']

    def init_candle_removed(self):

        self.candle_removed = int(config("CANDLE_REMOVED"))

        return True
    
    def get_candle_removed(self):

        return self.candle_removed

    async def get_candles_trends(self,candles):

        if len(candles) < self.candle_removed:

            return candles
        
        return candles[:self.candle_removed]
    
    async def get_candles_close(self,array_candles):

        return [candle['close'] for candle in array_candles]
    
    async def check_candles_trends(self,candles):

        if all(candles[i] < candles[i + 1] for i in range(len(candles) - 1)):

            return self.get_type_entry_long()  # Tendencia alcista

        if all(candles[i] > candles[i + 1] for i in range(len(candles) - 1)):

            return self.get_type_entry_short()  # Tendencia bajista

        return 0
    
    async def check_candles(self,candles):

        candles_trends = await self.get_candles_trends(candles['candles'])

        candles_trends_close = await self.get_candles_close(candles_trends)

        candles_trends_close = [1.32, 2.79, 3.33, 4.61, 5.45]

        result = await self.check_candles_trends(candles_trends_close)

        return True
    
    async def check_rsi(self,rsi): 

        if not(self.metrics_rsi['active']):

            return True

        if((self.metrics_rsi['min']<Decimal(rsi)) and (Decimal(rsi)<self.metrics_rsi['max'])):

            return True

        return False