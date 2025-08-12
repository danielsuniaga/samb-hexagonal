from decouple import config
from decimal import Decimal

class EntityMethodologyTrendsMinusML:
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

    def init_config(self):
        self.config = {
            'name': config("NAME_METHODOLOGY_TRENDS_MINUS_ML", default="TrendsMinusML"),
            'id': config("ID_METHODOLOGY_TRENDS_MINUS_ML", default=999)
        }
        return True

    def get_name(self):
        return self.config['name']

    def get_id(self):
        return self.config['id']

    def init_candle_removed(self):
        self.candle_removed = int(config("CANDLE_REMOVED_MINUS", default=3))
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
            'min': int(config("RSI_MIN", default=30)),
            'max': int(config("RSI_MAX", default=70)),
            'active': int(config("ACTIVE_RSI", default=1))
        }
        return True

    def init_metrics_sma(self):
        self.metrics_sma = {
            'active': int(config("ACTIVE_SMA", default=1))
        }
        return True

    def init_condition_entry(self):
        self.condition_entry = config("CONDITION_ENTRY", default="CLOSE")

    def get_condition_entry(self):
        return self.condition_entry

    def add_indicators(self, value):
        self.indicators = value
        return True

    def get_indicators(self):
        return self.indicators

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

    def get_candles_trends(self, candles):
        if len(candles) < self.candle_removed:
            return candles
        return candles[:self.candle_removed]

    def get_candles_close(self, array_candles):
        return [candle['close'] for candle in array_candles]

    def check_candles_trends(self, candles):
        if all(candles[i] < candles[i + 1] for i in range(len(candles) - 1)):
            self.set_type_entry(self.get_type_entry_long())
            return self.get_type_entry_long()
        if all(candles[i] > candles[i + 1] for i in range(len(candles) - 1)):
            self.set_type_entry(self.get_type_entry_short())
            return self.get_type_entry_short()
        return 0

    def check_candles(self, candles):
        candles_trends = self.get_candles_trends(candles['candles'])
        candles_trends_close = self.get_candles_close(candles_trends)
        # print(f"Checking candles trends: {candles_trends_close}")
        candles_trends_close = [1.32, 2.79, 3.33]
        result = self.check_candles_trends(candles_trends_close)
        return True

    def check_rsi(self, rsi):
        if not self.metrics_rsi['active']:
            return True
        if self.metrics_rsi['min'] < Decimal(rsi) < self.metrics_rsi['max']:
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
        if result_indicators.get('rsi') and result_indicators.get('sma_short') and result_indicators.get('sma_long'):
            return True
        return False

    def check_monetary_filters(self, monetary_filter):
        if monetary_filter['profit'] > monetary_filter['sum_entrys_dates'] and monetary_filter['loss'] < monetary_filter['sum_entrys_dates']:
            return True
        return False

    # --- ML específicos ---
    def get_methodology_description_number_by_id(self, id_methodology):
        return 42

    def check_predict_models(self, data_services):
        return True
