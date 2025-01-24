import apis.entities.reportsentrys.EntityReportEntrys as EntityReportEntrys

class ServicesReportEntrys():

    entity = None

    ServicesReports = None

    ServicesDates = None

    ServicesTelegram = None

    ServicesEntrysResults = None

    def __init__(self):

        self.entity = EntityReportEntrys.EntityReportEntrys()

    def init_services_reportsentrys(self, value):   

        self.ServicesEntrysResults = value

        return True

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
    
    def generate_message(self,data):

        return self.entity.generate_message(data)
    
    def send_message(self,mensaje):

        return self.ServicesTelegram.send_message_report(mensaje)
    
    def generate_data_report_cur(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_curdate(data)
    
    def generate_data_report_tot(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_total(data)
    
    def generate_data_report_nom(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_nom(data)
    
    def check_data_reports(self,data):

        if data['name'] == 'CUR':

            return self.generate_data_report_cur(data['data'])

        if data['name'] == 'TOT':   

            return self.generate_data_report_tot(data['data'])

        return self.generate_data_report_nom(data['data'])
    
    def generate_data_reports_daily(self):

        data = self.entity.get_data_reports()

        for item in data:

            item['data'] = self.check_data_reports(item)

        return data

    def get_daily_report_entrys(self):

        result_persistence=self.add_persistence_daily_reports_entrys()

        if not result_persistence['status']:

            return result_persistence
        
        data = self.generate_data_reports_daily()
        
        message = self.generate_message(data)
        
        return self.send_message(message)