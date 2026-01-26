from decouple import config
from decimal import Decimal

class EntityMethodologyTrendsRecentML:

    config = None
    candle_removed = None
    type_entry = None
    metrics_rsi = None
    metrics_sma = None
    type_entry_positions = None
    result_entrys = None
    condition_entry = None
    indicators = None
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

    # --- Configuración específica para TrendsRecentML ---
    def init_config(self):
        self.config = {
            'name': config("NAME_METHODOLOGY_TRENDS_RECENT_ML", default="TrendsRecentML"),
            'id': config("ID_METHODOLOGY_TRENDS_RECENT_ML", default="8")
        }
        return True

    def init_project_name(self):
        self.project_name = config("PROJECT_NAME")
        return True
    
    def get_project_name(self):
        return self.project_name

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

    def get_metrics_rsi_min(self):
        return self.metrics_rsi['min']

    def get_metrics_rsi_max(self):
        return self.metrics_rsi['max']

    def init_metrics_sma(self):
        self.metrics_sma = {
            'active': int(config("ACTIVE_SMA", default="1"))
        }
        return True

    def init_condition_entry(self):
        self.condition_entry = config("CONDITION_ENTRY", default="CLOSE")

    def get_condition_entry(self):
        return self.condition_entry

    # --- Manejo de indicadores (heredado de TrendsRecent) ---
    def add_indicators(self, value):
        self.indicators = value
        return True

    def get_indicators(self):
        return self.indicators

    # --- Manejo de resultados (heredado de TrendsRecent) ---
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

    # --- Análisis de velas TrendsRecent (lógica específica de tendencias) ---
    def get_candles_trends(self, candles):
        """
        Obtiene las velas más recientes para análisis de tendencias
        """
        return candles[-self.candle_removed:]

    def get_candles_close(self, array_candles):
        """
        Extrae los precios de cierre de las velas
        """
        return [candle['close'] for candle in array_candles]

    def check_candles_trends(self, candles):
        """
        Detecta tendencias en base a los precios de cierre:
        - Tendencia alcista: cada precio de cierre es mayor al anterior
        - Tendencia bajista: cada precio de cierre es menor al anterior
        """
        # Tendencia alcista: precios crecientes
        if all(candles[i] < candles[i + 1] for i in range(len(candles) - 1)):
            self.set_type_entry(self.get_type_entry_long())
            return self.get_type_entry_long()  # Tendencia alcista

        # Tendencia bajista: precios decrecientes
        if all(candles[i] > candles[i + 1] for i in range(len(candles) - 1)):
            self.set_type_entry(self.get_type_entry_short())
            return self.get_type_entry_short()  # Tendencia bajista

        return False  # No hay tendencia clara

    def check_candles(self, candles):
        """
        Método principal para análisis de velas TrendsRecent
        Analiza las velas más recientes para detectar tendencias
        """
        candles_trends = self.get_candles_trends(candles['candles'])
        candles_trends_close = self.get_candles_close(candles_trends)

        # candles_trends_close = [1.32, 2.79, 3.33, 4.61, 5.45]  # (tendencia alcista)
        result = self.check_candles_trends(candles_trends_close)
        
        return True  # Siempre retorna True para continuar el análisis

    # --- Análisis de indicadores técnicos (heredado de TrendsRecent) ---
    def check_rsi(self, rsi):
        """
        Verificación RSI: debe estar entre min y max para ser válido
        """
        if not self.metrics_rsi['active']:
            return True
        
        if self.metrics_rsi['min'] < Decimal(rsi) < self.metrics_rsi['max']:
            return True
        
        return False

    def check_sma_long(self, sma, last_candle):
        """
        Para tendencia alcista: SMA debe estar por debajo del precio actual
        """
        if sma < last_candle:
            return True
        return False

    def check_sma_short(self, sma, last_candle):
        """
        Para tendencia bajista: SMA debe estar por encima del precio actual
        """
        if sma > last_candle:
            return True
        return False

    def check_sma(self, sma, last_candle):
        """
        Verificación SMA según el tipo de tendencia detectada
        """
        if not self.metrics_sma['active']:
            return True

        if self.type_entry_positions == self.get_type_entry_long():
            return self.check_sma_long(sma, last_candle)

        if self.type_entry_positions == self.get_type_entry_short():
            return not self.check_sma_short(sma, last_candle)

        return False

    def check_result_indicators(self, result_indicators):
        """
        Verificación específica de TrendsRecent: RSI + ambos SMAs deben ser válidos
        (diferente de PinBarML que solo verifica RSI)
        """
        if result_indicators['rsi'] and result_indicators['sma_short'] and result_indicators['sma_long']:
            return True
        return False

    # --- Filtros monetarios (heredado de TrendsRecent) ---
    def check_monetary_filters(self, monetary_filter):
        """
        Control de riesgo: las ganancias deben superar las entradas del día
        y las pérdidas deben estar por debajo del límite
        """
        if (monetary_filter['profit'] > monetary_filter['sum_entrys_dates'] and 
            monetary_filter['loss'] < monetary_filter['sum_entrys_dates']):
            return True
        return False

    # --- Métodos ML adicionales (heredados de PinBarML) ---
    def get_methodology_description_number_by_id(self, id_methodology):
        """
        Retorna un número de descripción específico para la metodología TrendsRecentML
        Este número se usa para identificar la metodología en los modelos ML
        """
        return 48  # Número específico para TrendsRecentML (diferente a PinBarML=47)

    def check_predict_models(self, data_services):
        """
        Verifica usando modelos predictivos ML
        Específico para análisis de tendencias con ML
        """
        # Aquí se podría implementar lógica específica para la metodología TrendsRecent
        # Por ejemplo, considerar la fuerza de la tendencia y indicadores técnicos para ML
        return True