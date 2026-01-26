from decouple import config
from decimal import Decimal

class EntityMethodologyPinBar:
    config = None
    candle_removed = None
    data_candles = None
    indicators = None
    type_entry_positions = None
    type_entry = None
    metrics_rsi = None
    metrics_sma = None
    condition_entry = None
    result_entrys = None
    project_name = None

    def __init__(self):
        self.init_config()
        self.init_candle_removed()
        self.init_type_entry()
        self.init_metrics_rsi()
        self.init_metrics_sma()
        self.init_condition_entry()
        self.init_entrys_results()
        self.init_project_name()

    def init_project_name(self):
        self.project_name = config("PROJECT_NAME")
        return True
    
    def get_project_name(self):
        return self.project_name

    def init_entrys_results(self):
        self.result_entrys = {
            'result': None,
            'candles': None
        }
        return True

    def set_result_entrys_result(self, result_entrys):
        self.result_entrys['result'] = result_entrys
        return True

    def set_result_entrys_candles(self, result_candles):
        self.result_entrys['candles'] = result_candles
        return True

    def init_condition_entry(self):
        self.condition_entry = config("CONDITION_ENTRY")

    def init_metrics_sma(self):
        self.metrics_sma = {
            'active': int(config("ACTIVE_SMA"))
        }
        return True

    def get_metrics_sma(self, key):
        return self.metrics_sma[key]

    def get_metrics_sma_active(self):
        return self.get_metrics_sma('active')

    def init_metrics_rsi(self):
        self.metrics_rsi = {
            'min': int(config("RSI_MIN")),
            'max': int(config("RSI_MAX")),
            'active': int(config("ACTIVE_RSI"))
        }
        return True

    def get_metrics_rsi(self, key):
        return self.metrics_rsi[key]

    def get_metrics_rsi_min(self):
        return self.get_metrics_rsi('min')

    def get_metrics_rsi_max(self):
        return self.get_metrics_rsi('max')

    def get_metrics_rsi_active(self):
        return self.get_metrics_rsi('active')

    def get_type_entry_short(self):
        return self.type_entry['short']

    def get_type_entry_long(self):
        return self.type_entry['long']

    def get_type_entry_positions(self):
        return self.type_entry_positions

    def set_indicators(self, indicators):
        self.indicators = indicators
        return True

    def get_indicators(self):
        return self.indicators
    
    def add_indicators(self,value):
        self.indicators=value
        return True

    def set_data_candles(self, data_candles):
        self.data_candles = data_candles
        return True

    def get_data_candles(self):
        return self.data_candles

    def init_candle_removed(self):
        self.candle_removed = int(config("CANDLE_REMOVED"))
        return True

    def init_config(self):
        self.config = {
            'name': config("NAME_METHODOLOGY_PINBAR"),
            'id': config("ID_METHODOLOGY_PINBAR")
        }
        return True

    def get_condition_entry(self):
        return self.condition_entry

    def get_candle_removed(self):
        return self.candle_removed

    def get_id(self):
        return self.config['id']

    def get_name(self):
        return self.config['name']

    def get_candles_pinbar(self, candles):
        if len(candles) < self.candle_removed:
            return candles
        return candles[-self.candle_removed:]  # Trabajamos con las velas más recientes

    def generate_candles(self, candles):
        self.set_data_candles(self.get_candles_pinbar(candles['candles']))
        return True

    def set_type_entry(self, type_entry):
        self.type_entry_positions = type_entry
        return True

    def init_type_entry(self):
        self.type_entry = {
            'short': config("TYPE_ENTRY_SHORT"),
            'long': config("TYPE_ENTRY_LONG")
        }
        return True

    def check_candles_pinbar(self, candle):
        """
        Detecta patrones Pin Bar:
        - Pin Bar alcista (Hammer): Sombra inferior larga, cuerpo pequeño
        - Pin Bar bajista (Shooting Star): Sombra superior larga, cuerpo pequeño
        """
        # self.set_type_entry(self.get_type_entry_long())
        # return self.get_type_entry_long()

        # Calculamos las medidas de la vela
        body = abs(Decimal(candle['close']) - Decimal(candle['open']))
        total_range = Decimal(candle['high']) - Decimal(candle['low'])
        
        # Evitamos división por cero
        if total_range == 0:
            return False
        
        upper_shadow = Decimal(candle['high']) - max(Decimal(candle['open']), Decimal(candle['close']))
        lower_shadow = min(Decimal(candle['open']), Decimal(candle['close'])) - Decimal(candle['low'])

        # Criterios Pin Bar: sombra >= 66% del rango total, cuerpo <= 33% del rango total
        min_shadow_ratio = Decimal('0.66')
        max_body_ratio = Decimal('0.33')

        # Pin Bar alcista (Hammer): sombra inferior larga
        if (lower_shadow >= (total_range * min_shadow_ratio) and 
            body <= (total_range * max_body_ratio)):
            # print("Pin Bar alcista detectado (Hammer)")
            self.set_type_entry(self.get_type_entry_long())
            return self.get_type_entry_long()

        # Pin Bar bajista (Shooting Star): sombra superior larga
        if (upper_shadow >= (total_range * min_shadow_ratio) and 
            body <= (total_range * max_body_ratio)):
            # print("Pin Bar bajista detectado (Shooting Star)")
            self.set_type_entry(self.get_type_entry_short())
            return self.get_type_entry_short()

        return False

    def check_candles(self, candles):
        candle_list = candles.get('candles', [])
        # print(f"Pin Bar candles: {candle_list}")
        
        if len(candle_list) < 1:
            return False  # No hay velas para analizar

        # Analizamos la última vela para detectar Pin Bar
        last_candle = candle_list[-1]
        result = self.check_candles_pinbar(last_candle)
        
        if result:
            return result  # Devuelve el tipo de entrada encontrado
        
        return False  # No se encontró patrón Pin Bar

    def check_rsi(self, rsi):
        if not self.metrics_rsi['active']:
            return True
        if self.metrics_rsi['min'] < Decimal(rsi) < self.metrics_rsi['max']:
            return True
        return False

    def check_sma_long(self, sma, last_candle):
        if sma < last_candle:
            return True
        return False

    def check_sma_short(self, sma, last_candle):
        if sma > last_candle:
            return True
        return False

    def check_sma(self, sma, last_candle):
        if not self.metrics_sma['active']:
            return True
        
        if self.type_entry_positions == self.get_type_entry_long():
            return self.check_sma_long(sma, last_candle)
        
        if self.type_entry_positions == self.get_type_entry_short():
            return self.check_sma_short(sma, last_candle)

        return False

    def check_result_indicators(self, result_indicators):
        if result_indicators['rsi']:
            return True
        return False

    def check_monetary_filters(self, monetary_filter):
        if monetary_filter['profit'] > monetary_filter['sum_entrys_dates'] and monetary_filter['loss'] < monetary_filter['sum_entrys_dates']:
            return True
        return False

    def get_result_entrys_result(self):
        return self.result_entrys['result']
