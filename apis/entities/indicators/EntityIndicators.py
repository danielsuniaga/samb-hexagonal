from decouple import config

from decimal import Decimal

class EntityIndicators():

    indicators = None

    ids_indicators = None

    type_rsi = None

    candles_rsi = None

    sma_short = None

    sma_long = None

    candle_last = None
    
    def __init__(self):

        self.init_type_rsi()

        self.init_candles_rsi()

        self.init_sma_short()

        self.init_sma_long()

        self.init_candle_last()

        self.init_ids_indicators()

        self.init_indicators()

    def init_indicators(self):

        self.indicators = {
            'rsi10':{
                'id':config("RSI10"),
                'active':config("ACTIVE_RSI")
            },
            'sma10':{
                'id':config("SMA10"),
                'active':config("ACTIVE_SMA")
            },
            'sma30':{
                'id':config("SMA30"),
                'active':config("ACTIVE_SMA")
            }
        }

        return True
    
    def get_indicators(self):

        return self.indicators

    def init_ids_indicators(self):

        self.ids_indicators = {
            'rsi10':config("RSI10"),
            'sma10':config("SMA10"),
            'sma30':config("SMA30"),
        }

        return True
    
    def get_ids_indicators(self):
        
        return self.ids_indicators

    def init_sma_long(self):     

        self.sma_long = {
            'value':int(config("SMA_LONG")),
            'candle':int(config("CANDLE_SMA_LONG"))
        }

        return True
    
    def get_sma_long(self):

        return self.sma_long

    def init_candle_last(self):

        self.candle_last = int(config("CANDLE_LAST"))

        return True

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
    
    def get_candles_indicators(self,candles,candles_indicators):

        if len(candles) < candles_indicators:

            return candles
        
        return candles[:candles_indicators]
    
    def get_candles_close(self,array_candles):

        return [candle['close'] for candle in array_candles]
    
    def generate_rsi_entity(self,candles,periodos):

        gains = []

        losses = []

        # Calcular cambios en los precios y clasificar en ganancias y pérdidas
        for i in range(1, len(candles)):

            change = Decimal(candles[i]) - Decimal(candles[i - 1])

            if change > 0:

                gains.append(change)

                losses.append(Decimal('0'))

            elif change < 0:

                gains.append(Decimal('0'))

                losses.append(-change)

            else:

                gains.append(Decimal('0'))

                losses.append(Decimal('0'))

        # Usar Decimal para mantener consistencia de tipos
        avg_gain = sum(gains) / Decimal(str(periodos))  # Promedio de ganancias en los últimos períodos

        avg_loss = sum(losses) / Decimal(str(periodos))  # Promedio de pérdidas en los últimos períodos

        if avg_loss == 0:

            return Decimal('100')

        rs = avg_gain / avg_loss

        rsi = Decimal('100') - (Decimal('100') / (Decimal('1') + rs))

        return float(rsi)  # Convertir a float al final para compatibilidad

    def generate_rsi(self,candles):

        candles_rsi = self.get_candles_indicators(candles['candles'],self.candles_rsi)

        candles_rsi_close = self.get_candles_close(candles_rsi)

        return self.generate_rsi_entity(candles_rsi_close,self.type_rsi)
    
    def generate_sma_entity(self,candles,indicators):

        sma = sum(candles[-indicators:]) / indicators

        return sma
    
    def generate_sma(self,candles,indicators):

        candles_sma = self.get_candles_indicators(candles['candles'],indicators['candle'])

        candles_sma_close = self.get_candles_close(candles_sma)
        
        return self.generate_sma_entity(candles_sma_close,indicators['value'])
    
    def generate_candle_last(self,candles):

        candles_last = self.get_candles_indicators(candles['candles'],self.candle_last)

        candles_last_close = self.get_candles_close(candles_last)

        return candles_last_close[0]