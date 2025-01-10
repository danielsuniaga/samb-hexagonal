from datetime import datetime

import pytz

import time

class EntityDates():

    start_date = None

    def set_start_date(self):

        self.start_date = time.time()

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