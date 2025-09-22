from decouple import config
from decimal import Decimal

class EntityMethodologyTrendsMinusRecentML:

    config = None
    candle_removed = None
    type_entry = None
    type_entry_positions = None
    metrics_rsi = None
    metrics_sma = None
    indicators = None
    condition_entry = None
    result_entrys = None

    def __init__(self):
        self.init_config()
        self.init_candle_removed()  
        self.init_type_entry()
        self.init_metrics_rsi()
        self.init_metrics_sma()
        self.init_entrys_results()
        self.init_condition_entry()

    # --- Configuración base ---
    def init_config(self):
        self.config = {
            'name': config("NAME_METHODOLOGY_TRENDS_MINUS_RECENT_ML", default="TrendsMinusRecentML"),
            'id': config("ID_METHODOLOGY_TRENDS_MINUS_RECENT_ML", default=49)
        }
        return True
    
    def get_name(self):
        return self.config['name']

    def get_id(self):
        return self.config['id']

    # --- Configuración de velas ---
    def init_candle_removed(self):
        self.candle_removed = int(config("CANDLE_REMOVED_MINUS", default=3))
        return True

    def get_candle_removed(self):
        return self.candle_removed

    # --- Configuración de tipos de entrada ---
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

    # --- Configuración de métricas RSI ---
    def init_metrics_rsi(self):
        self.metrics_rsi = {
            'min': int(config("RSI_MIN", default=30)),
            'max': int(config("RSI_MAX", default=70)),
            'active': int(config("ACTIVE_RSI", default=1))
        }
        return True

    # --- Configuración de métricas SMA ---
    def init_metrics_sma(self):
        self.metrics_sma = {
            'active': int(config("ACTIVE_SMA", default=1))
        }
        return True

    # --- Configuración de condición de entrada ---
    def init_condition_entry(self):
        self.condition_entry = config("CONDITION_ENTRY", default="CLOSE")

    def get_condition_entry(self):
        return self.condition_entry

    # --- Gestión de indicadores ---
    def add_indicators(self, value):
        self.indicators = value
        return True
    
    def get_indicators(self):
        return self.indicators

    # --- Gestión de resultados de entrada ---
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

    # --- Análisis de velas (lógica TrendsMinusRecent) ---
    def get_candles_trends(self, candles):
        """
        TrendsMinusRecent usa las últimas N velas (desde el final)
        Diferente a TrendsMinus que usa las primeras N velas
        """
        return candles[-self.candle_removed:]
    
    def get_candles_close(self, array_candles):
        return [candle['close'] for candle in array_candles]
    
    def check_candles_trends(self, candles):
        """
        Análisis de tendencias secuenciales:
        - Tendencia alcista: cada vela cierra más alto que la anterior
        - Tendencia bajista: cada vela cierra más bajo que la anterior
        """
        # self.set_type_entry(self.get_type_entry_long())
        # return self.get_type_entry_long()  # Tendencia alcista
        if all(candles[i] < candles[i + 1] for i in range(len(candles) - 1)):
            self.set_type_entry(self.get_type_entry_long())
            return self.get_type_entry_long()  # Tendencia alcista

        if all(candles[i] > candles[i + 1] for i in range(len(candles) - 1)):
            self.set_type_entry(self.get_type_entry_short())
            return self.get_type_entry_short()  # Tendencia bajista

        return 0
    
    def check_candles(self, candles):
        """
        Método principal de análisis de velas
        Utiliza lógica TrendsMinusRecent (últimas N velas)
        """
        candles_trends = self.get_candles_trends(candles['candles'])
        candles_trends_close = self.get_candles_close(candles_trends)
        result = self.check_candles_trends(candles_trends_close)
        return True
    
    # --- Verificación de indicadores ---
    def check_rsi(self, rsi): 
        if not self.metrics_rsi['active']:
            return True

        if (self.metrics_rsi['min'] < Decimal(rsi) < self.metrics_rsi['max']):
            return True

        return False
    
    def check_sma_long(self, sma, last_candle):   
        return sma < last_candle
    
    def check_sma_short(self, sma, last_candle):
        return sma > last_candle
    
    def check_sma(self, sma, last_candle):
        if not self.metrics_sma['active']:
            return True
        
        if self.type_entry_positions == self.get_type_entry_long():
            return self.check_sma_long(sma, last_candle)
        
        if self.type_entry_positions == self.get_type_entry_short():
            return not self.check_sma_short(sma, last_candle)

        return False
    
    def check_result_indicators(self, result_indicators):
        """
        Validación completa de indicadores:
        - RSI debe estar en rango válido
        - SMA short debe confirmar dirección de tendencia  
        - SMA long debe confirmar dirección de tendencia
        """
        if result_indicators['rsi'] and result_indicators['sma_short'] and result_indicators['sma_long']:
            return True
        
        return False
    
    # --- Filtros monetarios ---
    def check_monetary_filters(self, monetary_filter):
        """
        Filtro de gestión de riesgo:
        - Ganancias esperadas > pérdidas actuales del día
        - Pérdidas potenciales < límite de pérdidas del día
        """
        if (monetary_filter['profit'] > monetary_filter['sum_entrys_dates'] and 
            monetary_filter['loss'] < monetary_filter['sum_entrys_dates']):
            return True
        
        return False

    # --- Métodos ML adicionales (heredados de TrendsMinusML) ---
    def get_methodology_description_number_by_id(self, id_methodology):
        """
        ID numérico para identificación en modelos ML
        TrendsMinusRecentML tiene ID único para diferenciarlo
        """
        return 49  # ID único para TrendsMinusRecentML

    def check_predict_models(self, data_services):
        """
        Verificación de modelos predictivos ML
        Placeholder para integración con servicios de ML
        """
        return True