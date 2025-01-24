import apis.entities.reportsentrys.EntityReportEntrys as EntityReportEntrys

class ServicesReportEntrys():

    entity = None

    ServicesReports = None

    ServicesDates = None

    ServicesTelegram = None

    def __init__(self):

        self.entity = EntityReportEntrys.EntityReportEntrys()

    def init_services_telegram(self, value):    

        self.ServicesTelegram = value

        return True

    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()

    def init_services_reports(self, value):

        self.ServicesReports = value

        return True
    
    def init_services_dates(self, value):

        self.ServicesDates = value

        return True
    
    def get_types_reports_daily(self):

        return self.entity.get_types_reports_daily()
    
    def add_persistence_daily_reports_entrys(self):

        type_reports = self.get_types_reports_daily()

        return self.ServicesReports.add_persistence(type_reports,self.get_current_date_hour())
    
    def generate_message(self):

        return self.entity.generate_message()
    
    def send_message(self,mensaje):

        return self.ServicesTelegram.send_message_report(mensaje)
    
    def generate_data_report_cur(self,data):

        return True
    
    def generate_data_report_tot(self,data):

        return True
    
    def generate_data_report_nom(self,data):

        return True
    
    def check_data_reports(self,data):

        for item in data:

            if item['name'] == 'CUR':

                return self.generate_data_report_cur(item['data'])

            if item['name'] == 'TOT':   

                return self.generate_data_report_tot(item['data'])

            return self.generate_data_report_nom(item['data'])
        
        return False
    
    def generate_data_reports_daily(self):

        data = self.entity.get_data_reports()

        for item in data:

            item['data'] = self.check_data_reports(item)

        print(data)

        return True

    def get_daily_report_entrys(self):

        result_persistence=self.add_persistence_daily_reports_entrys()

        if not result_persistence['status']:

            return result_persistence
        
        data = self.generate_data_reports_daily()
        
        message = self.generate_message()
        
        return self.send_message(message)