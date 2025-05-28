import apis.entities.reportscrons.EntityReportsCrons as EntityReportsCrons  

class ServicesReportCrons():

    entity = None

    ServicesDates = None

    ServicesReports = None

    ServicesCronjobs = None

    ServicesTelegram = None

    ServicesDeriv = None

    ServicesEvents = None

    def __init__(self):

        self.entity = EntityReportsCrons.EntityReportsCrons()

    def init_services_events(self, value):

        self.ServicesEvents = value

        return True

    def init_services_deriv(self, value):

        self.ServicesDeriv = value

        return True

    def init_services_telegram(self, value):

        self.ServicesTelegram = value

        return True

    def init_services_cronjobs(self, value):

        self.ServicesCronjobs = value

        return True

    def init_services_reports(self, value):

        self.ServicesReports = value

        return True

    def init_services_dates(self, value):

        self.ServicesDates = value

        return True

    def get_types_reports_daily(self):

        return self.entity.get_types_reports_daily()
    
    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()
    
    def add_persistence_daily_reports_crons(self):

        type_reports = self.get_types_reports_daily()

        return self.ServicesReports.add_persistence(type_reports,self.get_current_date_hour())
    
    def get_data_cronjobs_curdate(self,data):

        return self.ServicesCronjobs.get_data_cronjobs_curdate(data)
    
    def get_data_reports(self):

        return self.entity.get_data_reports()
    
    def check_data_reports(self,data):

        result = self.get_data_cronjobs_curdate(data)

        return result
    
    def generate_data_reports_daily_events(self):

        return self.ServicesEvents.get_events_daily_cron()
    
    def generate_data_reports_daily(self):

        data = self.get_data_reports()

        for item in data:

            item = self.check_data_reports(item)

        return data
    
    def generate_message(self,data,duration_seconds):

        return self.entity.generate_message(data,duration_seconds)
    
    def generate_message_events(self,data_events):

        return self.entity.generate_message_events(data_events)
    
    def send_message(self,mensaje):

        return self.ServicesTelegram.send_message_report(mensaje)

    def get_daily_report_crons(self):

        result_persistence = self.add_persistence_daily_reports_crons()

        if not result_persistence['status']:

            return result_persistence
        
        data = self.generate_data_reports_daily()

        data_events = self.generate_data_reports_daily_events()

        duration_seconds = self.get_duration_seconds()

        message = self.generate_message(data,duration_seconds)  + self.generate_message_events(data_events)
        
        return self.send_message(message)
    
    def get_duration_seconds(self):

        return self.ServicesDeriv.get_duration_seconds()