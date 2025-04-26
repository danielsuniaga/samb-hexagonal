import apis.entities.reportsentrys.EntityReportEntrys as EntityReportEntrys

class ServicesReportEntrys():

    entity = None

    ServicesReports = None

    ServicesDates = None

    ServicesTelegram = None

    ServicesEntrysResults = None

    ServicesMethodologys = None

    ServicesManagerDays = None

    def __init__(self):

        self.entity = EntityReportEntrys.EntityReportEntrys()

    def init_services_manager_days(self,value):

        self.ServicesManagerDays = value

        return True

    def init_data_reports(self):    

        self.entity.init_data_reports()

        return True

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
    
    def generate_message(self,data,name_methodology):

        return self.entity.generate_message(data,name_methodology)
    
    def generate_message_parameters(self,data):
            
        return self.entity.generate_message_parameters(data)
    
    def send_message(self,mensaje):

        return self.ServicesTelegram.send_message_report(mensaje)
    
    def generate_data_report_cur(self,data,id_methodology):

        return self.ServicesEntrysResults.get_data_entrys_results_curdate(data,id_methodology)
    
    def generate_data_report_cur_complete(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_curdate_complete(data)
    
    def generate_data_report_tot(self,data,id_methodology):

        return self.ServicesEntrysResults.get_data_entrys_results_total(data,id_methodology)
    
    def generate_data_report_tot_complete(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_total_complete(data)
    
    def generate_data_report_nom(self,data,id_methodology):

        return self.ServicesEntrysResults.get_data_entrys_results_nom(data,id_methodology)
    
    def generate_data_report_nom_complete(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_nom_complete(data)
    
    def check_data_reports(self,data,id_methodology):

        if data['name'] == 'CUR':

            return self.generate_data_report_cur(data['data'],id_methodology)

        if data['name'] == 'TOT':   

            return self.generate_data_report_tot(data['data'],id_methodology)

        return self.generate_data_report_nom(data['data'],id_methodology)
    
    def check_data_reports_complete(self,data):

        if data['name'] == 'CUR':

            return self.generate_data_report_cur_complete(data['data'])

        if data['name'] == 'TOT':   

            return self.generate_data_report_tot_complete(data['data'])

        return self.generate_data_report_nom_complete(data['data'])
    
    def generate_data_reports_daily(self,id_methodology):

        data = self.entity.get_data_reports()

        for item in data:

            item = self.check_data_reports(item,id_methodology)
            
        return data
    
    def get_methodologys(self):

        return self.ServicesMethodologys.get_methodologys()
    
    def generate_data_reports_daily_complete(self):

        data = self.entity.get_data_reports()

        for item in data:

            item = self.check_data_reports_complete(item)
            
        return data
    
    def get_titles_reports_daily_complete_complement(self):

        return self.entity.get_titles_reports_daily_complete_complement()
    
    def init_message_params(self):

        return self.entity.init_message_params()
    
    def get_daily_report_entrys_complete(self):

        self.init_data_reports()

        self.init_message_params()

        data = self.generate_data_reports_daily_complete()

        message = self.generate_message(data,self.get_titles_reports_daily_complete_complement())

        result = self.send_message(message)

        return True
    
    def get_day(self):

        return self.ServicesDates.get_day()
    
    def get_type_manager_days_reporting(self,day,id_methodology):

        return self.ServicesManagerDays.get_type_manager_days_reporting(day,id_methodology)
    
    def set_message_params(self,message):
           
        return self.entity.set_message_params(message)

    def get_daily_report_entrys(self):

        result_persistence=self.add_persistence_daily_reports_entrys()

        if not result_persistence['status']:

            return result_persistence
        
        methodologys = self.get_methodologys()

        result = []

        day = self.get_day()
        
        for item in methodologys:

            self.init_data_reports()

            data_param = self.get_type_manager_days_reporting(day,item['id'])

            message_param = self.generate_message_parameters(data_param)

            self.set_message_params(message_param)

            data = self.generate_data_reports_daily(item['id'])

            message = self.generate_message(data,item['descriptions'])

            result = self.send_message(message)

        self.get_daily_report_entrys_complete()
        
        return result
