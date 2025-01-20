class EntityEvents():

    events = None

    def __init__(self):

        self.init_events()

    def init_events(self):

        self.events = self.init_data_events_empty()

        return True
    
    def get_events(self):

        return self.events

    def init_data_events_empty(self):

        return {
            'start_endpoint': '',
            'init_endpoint': '',
            'init_broker': '',
            'config_broker': '',
            'init_loop':'',
            'get_candles':'',
            'check_candles':'',
            'generate_indicators':'',
            'get_filter_monetary':'',
            'get_model_general_rl':'',
            'add_positions_brokers':'',
            'add_persistence':''
        }

    def set_events_field(self,field,value):

        self.events[field] = value

        return True