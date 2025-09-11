from decouple import config
from decimal import Decimal

class EntityMethodologyWMARecentML:

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

    def __init__(self):
        self.init_config()
        self.init_candle_removed()
        self.init_type_entry()
        self.init_metrics_rsi()
        self.init_metrics_sma()
        self.init_condition_entry()
        self.init_entrys_results()

    # --- Configuración específica para WMARecentML ---
    def init_config(self):
        self.config = {
            'name': config("NAME_METHODOLOGY_WMA_RECENT_ML", default="WMARecentML"),
            'id': config("ID_METHODOLOGY_WMA_RECENT_ML", default="6")
        }
        return True

    def get_name(self):
        return self.config['name']

    def get_id(self):
        return self.config['id']

    def init_candle_removed(self):
        self.candle_removed = int(config("CANDLE_REMOVED", default="2"))
        return True

    def get_candle_removed(self):
        return self.candle_removed

    def init_type_entry(self):
        self.type_entry = {
            'short': config("TYPE_ENTRY_SHORT", default="PUT"),
            'long': config("TYPE_ENTRY_LONG", default="CALL")
        }
        return True

    def get_type_entry_short(self):
        return self.type_entry['short']

    def get_type_entry_long(self):
        return self.type_entry['long']

    def get_type_entry_positions(self):
        return self.type_entry_positions

    def set_type_entry(self, type_entry):
        self.type_entry_positions = type_entry
        return True

    def init_metrics_rsi(self):
        self.metrics_rsi = {
            'min': int(config("RSI_MIN", default="30")),
            'max': int(config("RSI_MAX", default="70")),
            'active': int(config("ACTIVE_RSI", default="1"))
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

    def init_metrics_sma(self):
        self.metrics_sma = {
            'active': int(config("ACTIVE_SMA", default="1"))
        }
        return True

    def get_metrics_sma(self, key):
        return self.metrics_sma[key]

    def get_metrics_sma_active(self):
        return self.get_metrics_sma('active')

    def init_condition_entry(self):
        self.condition_entry = config("CONDITION_ENTRY", default="CLOSE")

    def get_condition_entry(self):
        return self.condition_entry

    # --- Manejo de indicadores (heredado de WMARecent) ---
    def set_indicators(self, indicators):
        self.indicators = indicators
        return True

    def get_indicators(self):
        return self.indicators

    # --- Manejo de datos de velas (específico de WMA Recent) ---
    def set_data_candles(self, data_candles):
        self.data_candles = data_candles
        return True

    def get_data_candles(self):
        return self.data_candles

    # --- Manejo de resultados ---
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

    def get_result_entrys_result(self):
        return self.result_entrys['result']

    # --- Análisis de velas WMA (lógica específica de WMA Recent) ---
    def get_candles_wma(self, candles):
        return candles[-self.candle_removed:]

    def generate_candles(self, candles):
        self.set_data_candles(self.get_candles_wma(candles['candles']))
        return True

    def check_candles_wma(self, data):
        """
        Lógica específica de WMA Recent:
        - Verifica si SMA short está entre open y close price
        - Determina dirección LONG o SHORT basado en la posición
        """
        # self.set_type_entry(self.get_type_entry_long())
        # return self.get_type_entry_long()
        if Decimal(data['open_price']) <= Decimal(data['sma_short']) <= Decimal(data['close_price']):
            # LONG - precio sube y SMA está en el medio
            self.set_type_entry(self.get_type_entry_long())
            return self.get_type_entry_long()
        
        if Decimal(data['close_price']) <= Decimal(data['sma_short']) <= Decimal(data['open_price']):
            # SHORT - precio baja y SMA está en el medio
            self.set_type_entry(self.get_type_entry_short())
            return self.get_type_entry_short()
        
        return False

    def check_candles(self):
        """
        Verifica patrones WMA en las velas recientes
        Itera sobre las velas para encontrar el patrón
        """
        candles = self.get_data_candles()
        indicators = self.get_indicators()

        for candle in candles:
            data = {}
            data['open_price'] = candle['open']
            data['close_price'] = candle['close']
            data['sma_short'] = indicators['sma_short']

            result = self.check_candles_wma(data)
            if result:
                break

        return True

    # --- Análisis de indicadores técnicos (heredado con defaults ML) ---
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
        """
        Verificación SMA con lógica específica de WMA Recent
        """
        if not self.metrics_sma['active']:
            return True
        
        if self.type_entry_positions == self.get_type_entry_long():
            return self.check_sma_long(sma, last_candle)
        
        if self.type_entry_positions == self.get_type_entry_short():
            return self.check_sma_short(sma, last_candle)

        return False

    def check_result_indicators(self, result_indicators):
        """
        Verificación específica de WMA Recent: verifica RSI y ambos SMAs
        (diferente de EnvolventML que solo verifica RSI)
        """
        if result_indicators['rsi'] and result_indicators['sma_short'] and result_indicators['sma_long']:
            return True
        return False

    # --- Filtros monetarios ---
    def check_monetary_filters(self, monetary_filter):
        if monetary_filter['profit'] > monetary_filter['sum_entrys_dates'] and monetary_filter['loss'] < monetary_filter['sum_entrys_dates']:
            return True
        return False

    # --- Métodos ML adicionales (heredados de EntityMethodologyEnvolventML) ---
    def get_methodology_description_number_by_id(self, id_methodology):
        """
        Retorna un número de descripción específico para la metodología WMARecentML
        Este número se usa para identificar la metodología en los modelos ML
        """
        return 46  # Número específico para WMARecentML (diferente a otros)

    def check_predict_models(self, data_services):
        """
        Verifica usando modelos predictivos ML
        Específico para patrones WMA Recent con ML
        """
        # Aquí se podría implementar lógica específica para la metodología WMA Recent
        # Por ejemplo, considerar patrones WMA y SMA en los datos para ML
        return True
