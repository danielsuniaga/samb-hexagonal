from decouple import config

from decimal import Decimal

class EntityIndicators():

    type_rsi = None

    candles_rsi = None

    sma_short = None

    def __init__(self):

        self.init_type_rsi()

        self.init_candles_rsi()

        self.init_sma_short()

    def init_sma_short(self):

        self.sma_short = {
            'value':int(config("SMA_SHORT")),
            'candle':int(config("CANDLE_SMA_SHORT"))
        }

        return True

    def get_sma_short(self):

        return self.sma_short

    def init_type_rsi(self):

        self.type_rsi = int(config("TYPE_RSI"))

        return True
    
    def init_candles_rsi(self):

        self.candles_rsi = int(config("CANDLE_RSI"))

        return True
    
    async def get_candles_indicators(self,candles,candles_indicators):

        if len(candles) < candles_indicators:

            return candles
        
        return candles[:candles_indicators]
    
    async def get_candles_close(self,array_candles):

        return [candle['close'] for candle in array_candles]
    
    async def generate_rsi_entity(self,candles,periodos):

        gains = []

        losses = []

        # Calcular cambios en los precios y clasificar en ganancias y pérdidas
        for i in range(1, len(candles)):

            change = Decimal(candles[i]) - Decimal(candles[i - 1])

            if change > 0:

                gains.append(change)

                losses.append(0)

            elif change < 0:

                gains.append(0)

                losses.append(-change)

            else:

                gains.append(0)

                losses.append(0)

        avg_gain = sum(gains) / periodos  # Promedio de ganancias en los últimos 10 períodos

        avg_loss = sum(losses) / periodos  # Promedio de pérdidas en los últimos 10 períodos

        # Evitar división por cero
        if avg_loss == 0:

            return 100

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi

    async def generate_rsi(self,candles):

        candles_rsi = await self.get_candles_indicators(candles['candles'],self.candles_rsi)

        candles_rsi_close = await self.get_candles_close(candles_rsi)

        return await self.generate_rsi_entity(candles_rsi_close,self.type_rsi)
    
    async def generate_sma(self,candles,indicators):

        print("candles",candles,"indicators",indicators)
        
        return True