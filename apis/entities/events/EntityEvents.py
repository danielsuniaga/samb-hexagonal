import uuid

from datetime import datetime

class EntityEvents():

    events = None

    config = None

    def __init__(self):

        self.init_events()

        self.init_config()

    def init_config(self):

        self.config = {
            'conditioon': '1'
        }

        return True
    
    def get_config(self,key):

        if not self.config:

            self.init_config()

        return self.config[key] 
    
    def get_config_condition(self): 

        return self.get_config('conditioon')

    def generate_id(self):

        return uuid.uuid4().hex

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
    
    def generate_diferences_events(self):

        event_data = self.get_events()

        differences = self.calculate_event_differences(event_data)

        return differences

    def calculate_event_differences(self, event_data):

        differences = {}

        previous_time = None

        for event, timestamp in event_data.items():

            differences[event] = self.calculate_difference_for_event(timestamp, previous_time)

            if timestamp:

                previous_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

        return differences

    def calculate_difference_for_event(self, timestamp, previous_time):

        if not timestamp:

            return None  # No timestamp to calculate difference

        current_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
        
        if previous_time:

            return (current_time - previous_time).total_seconds() * 1000  # Convert to milliseconds

        return None