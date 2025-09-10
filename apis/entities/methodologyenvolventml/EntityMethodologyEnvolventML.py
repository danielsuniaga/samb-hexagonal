from decouple import config
from decimal import Decimal

class EntityMethodologyEnvolventML:

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

    # --- Configuración específica para EnvolventML ---
    def init_config(self):
        self.config = {
            'name': config("NAME_METHODOLOGY_ENVOLVENT_ML", default="EnvolventML"),
            'id': config("ID_METHODOLOGY_ENVOLVENT_ML", default="5")
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

    # --- Manejo de indicadores (método específico de envolvente) ---
    def set_indicators(self, indicators):
        self.indicators = indicators
        return True

    def get_indicators(self):
        return self.indicators

    # --- Manejo de datos de velas (específico de envolvente) ---
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

    # --- Análisis de velas envolventes (lógica específica de envolvente) ---
    def get_candles_envolvent(self, candles):
        if len(candles) < self.candle_removed:
            return candles
        return candles[:self.candle_removed]

    def generate_candles(self, candles):
        self.set_data_candles(self.get_candles_envolvent(candles['candles']))
        return True

    def check_candles_envolvent(self, prev_candle, curr_candle):
        """
        Lógica específica de patrones envolventes:
        - Patrón envolvente alcista
        - Patrón envolvente bajista
        """
        # Patrón envolvente alcista
        if Decimal(curr_candle['open']) < Decimal(curr_candle['close']) and \
           Decimal(prev_candle['open']) > Decimal(prev_candle['close']) and \
           Decimal(curr_candle['open']) < Decimal(prev_candle['close']) and \
           Decimal(curr_candle['close']) > Decimal(prev_candle['open']):
            self.set_type_entry(self.get_type_entry_long())
            return self.get_type_entry_long()
        
        # Patrón envolvente bajista
        if Decimal(curr_candle['open']) > Decimal(curr_candle['close']) and \
           Decimal(prev_candle['open']) < Decimal(prev_candle['close']) and \
           Decimal(curr_candle['open']) > Decimal(prev_candle['close']) and \
           Decimal(curr_candle['close']) < Decimal(prev_candle['open']):
            self.set_type_entry(self.get_type_entry_short())
            return self.get_type_entry_short()
        
        return False

    def check_candles(self, candles):
        """
        Verifica patrones envolventes en las velas
        """
        candle_list = candles.get('candles', [])
        if len(candle_list) < 2:
            return False  # No hay suficientes velas    
        
        prev_candle = candle_list[-2]
        curr_candle = candle_list[-1]
        result = self.check_candles_envolvent(prev_candle, curr_candle)
        
        if result:
            return result  # Devuelve el tipo de entrada encontrado
        return False  # No se encontró un patrón envolvente

    # --- Análisis de indicadores técnicos ---
    def check_rsi(self, rsi):
        if not self.metrics_rsi['active']:
            return True
        if self.metrics_rsi['min'] < Decimal(rsi) < self.metrics_rsi['max']:
            return True
        return False

    def check_sma(self, sma, last_candle):
        """
        Verificación SMA con lógica específica de envolvente
        """
        if not self.get_metrics_sma_active():
            return True
        
        # Lógica específica basada en el tipo de entrada detectado por envolvente
        if self.type_entry_positions == self.get_type_entry_long():
            return sma < last_candle  # Para CALL, SMA debe estar por debajo
        
        if self.type_entry_positions == self.get_type_entry_short():
            return sma > last_candle  # Para PUT, SMA debe estar por encima

        return False

    def check_result_indicators(self, result_indicators):
        """
        Verificación específica de envolvente: solo verifica RSI
        (diferente de otras metodologías que verifican múltiples indicadores)
        """
        if result_indicators['rsi']:
            return True
        return False

    # --- Filtros monetarios ---
    def check_monetary_filters(self, monetary_filter):
        if monetary_filter['profit'] > monetary_filter['sum_entrys_dates'] and monetary_filter['loss'] < monetary_filter['sum_entrys_dates']:
            return True
        return False

    # --- Métodos ML adicionales (heredados de EntityMethodologyTrendsExpansiveML) ---
    def get_methodology_description_number_by_id(self, id_methodology):
        """
        Retorna un número de descripción específico para la metodología EnvolventML
        Este número se usa para identificar la metodología en los modelos ML
        """
        return 45  # Número específico para EnvolventML (diferente a otros)

    def check_predict_models(self, data_services):
        """
        Verifica usando modelos predictivos ML
        Específico para patrones envolventes con ML
        """
        # Aquí se podría implementar lógica específica para la metodología envolvente
        # Por ejemplo, considerar patrones envolventes en los datos para ML
        return True
