from decouple import config

class EntityMethodologyWMA:

    config = None

    candle_removed = None

    data_candles = None

    indicators = None

    type_entry_positions = None

    type_entry = None

    def __init__(self):

        self.init_config()

        self.init_candle_removed()

        self.init_type_entry()

    def get_type_entry_short(self):

        return self.type_entry['short']
    
    def get_type_entry_long(self):

        return self.type_entry['long']


    def set_indicators(self,indicators):

        self.indicators = indicators

        return True
    
    def get_indicators(self):

        return self.indicators

    def set_data_candles(self,data_candles):

        self.data_candles = data_candles

        return True
    
    def get_data_candles(self):

        return self.data_candles

    def init_candle_removed(self):

        self.candle_removed = int(config("CANDLE_REMOVED"))

        return True

    def init_config(self):

        self.config = {
            'name':config("NAME_METHODOLOGY_WMA"),
            'id':config("ID_METHODOLOGY_WMA")
        }

        return True
    
    def get_id(self):

        return self.config['id'] 
    
    def get_candles_wma(self,candles):

        if len(candles) < self.candle_removed:

            return candles
        
        return candles[:self.candle_removed]

    def generate_candles(self,candles):

        self.set_data_candles(self.get_candles_wma(candles['candles']))
        
        return True 
    
    def set_type_entry(self,type_entry):
        
        self.type_entry_positions = type_entry

        return True
    
    def init_type_entry(self):

        self.type_entry = {
            'short':config("TYPE_ENTRY_SHORT"),
            'long':config("TYPE_ENTRY_LONG")
        }

        return True
    
    def check_candles_wma(self,data):

        data = {
            'open_price': 1.0,
            'close_price': 3.0,
            'sma_long': 2.0
        }

        if data['open_price'] <= data['sma_long'] <= data['close_price']:

            # long

            self.set_type_entry(self.get_type_entry_long())

            return self.get_type_entry_long()
        
        if data['close_price'] <= data['sma_long'] <= data['open_price']:

            # SHORT

            self.set_type_entry(self.get_type_entry_short())
            
            return self.get_type_entry_short()
        
        return False
    
    def check_candles(self):

        candles = self.get_data_candles()

        indicators = self.get_indicators()

        for candle in candles:

            data = {}
            
            data['open_price'] = candle['open']

            data['close_price'] = candle['close']

            data['sma_long'] = indicators['sma_long']

            result = self.check_candles_wma(data)

            if result:

                break

        return True