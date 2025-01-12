from datetime import datetime

import pytz

import time

class EntityDates():

    dates_endpoints = None

    def __init__(self):

        self.init_dates_endpoints()

    def init_dates_endpoints(self):

        self.dates_endpoints = {
            'start':time.time(),
            'end':time.time()
        }

        return True

    def set_start_date(self):

        self.dates_endpoints['start'] = time.time()

        return True
    
    def set_end_date(self):

        self.dates_endpoints['end'] = time.time()

        return True

    def get_current_utc5(self):

        now_utc = datetime.now(pytz.utc)

        tz = pytz.timezone('America/Bogota')  # Puedes cambiar 'America/New_York' por la zona horaria deseada
        
        return now_utc.astimezone(tz)
    
    def get_current_date_mil_front(self,date):

        return date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    def get_current_date_mil_dynamic(self):

        now = self.get_current_utc5()

        return self.get_current_date_mil_front(now)
    
    def get_current_date(self,date):

        return date.strftime("%Y%m%d%H%M%S")
    
    def get_current_hour(self,hour):

        return hour.strftime("%H%M%S")
    
    def get_current_date_only(self):

        now = self.get_current_utc5()

        return now.strftime("%Y%m%d")
    
    def get_current_date_hour(self):

        now = self.get_current_utc5()

        return now.strftime("%Y%m%d%H%M%S")
    
    def get_day(self):

        now = self.get_current_utc5()

        return now.weekday()
    
    def get_time_execution(self):

        return self.dates_endpoints['end'] - self.dates_endpoints['start']