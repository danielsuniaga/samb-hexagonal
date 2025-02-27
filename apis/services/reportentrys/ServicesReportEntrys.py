import apis.entities.reportsentrys.EntityReportEntrys as EntityReportEntrys

class ServicesReportEntrys():

    entity = None

    ServicesReports = None

    ServicesDates = None

    ServicesTelegram = None

    ServicesEntrysResults = None

    ServicesMethodologys = None

    def __init__(self):

        self.entity = EntityReportEntrys.EntityReportEntrys()

    def init_services_methodologys(self, value):

        self.ServicesMethodologys = value

        return True

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
    
    def generate_data_report_cur(self,data,id_methodology):

        return self.ServicesEntrysResults.get_data_entrys_results_curdate(data,id_methodology)
    
    def generate_data_report_tot(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_total(data)
    
    def generate_data_report_nom(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_nom(data)
    
    def check_data_reports(self,data,id_methodology):

        if data['name'] == 'CUR':

            return self.generate_data_report_cur(data['data'],id_methodology)

        if data['name'] == 'TOT':   

            return self.generate_data_report_tot(data['data'])

        return self.generate_data_report_nom(data['data'])
    
    def generate_data_reports_daily(self,id_methodology):

        data = self.entity.get_data_reports()

        for item in data:

            item = self.check_data_reports(item,id_methodology)

        return data
    
    def get_methodologys(self):

        return self.ServicesMethodologys.get_methodologys()

    def get_daily_report_entrys(self):

        result_persistence=self.add_persistence_daily_reports_entrys()

        if not result_persistence['status']:

            return result_persistence
        
        methodologys = self.get_methodologys()

        result = []
        
        for item in methodologys:

            data = self.generate_data_reports_daily(item['id'])

            message = self.generate_message(data)

            result = self.send_message(message)
        
        return result
