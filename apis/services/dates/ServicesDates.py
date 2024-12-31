import apis.entities.dates.EntityDates as EntityDates

class ServicesDate(): 

    entity = None

    def __init__(self):

        self.entity = EntityDates.EntityDates()

    def get_current_utc5(self):

        return self.entity.get_current_utc5()
    
    def set_start_date(self):

        return self.entity.set_start_date()

    def get_current_date_mil_dynamic(self):

        return self.entity.get_current_date_mil_dynamic()
    
    def get_current_date(self,now):

        return self.entity.get_current_date(now)
    
    def get_current_hour(self,now):

        return self.entity.get_current_hour(now)
    
    def get_day(self):

        return self.entity.get_day()