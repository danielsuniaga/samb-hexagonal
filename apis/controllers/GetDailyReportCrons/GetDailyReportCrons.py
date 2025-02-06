import apis.services.reportcrons.ServicesReportCrons as ServicesReportCrons
import apis.services.dates.ServicesDates as ServicesDates 
import apis.services.reports.ServicesReports as ServicesReports
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs

class ControllerGetDailyReportCrons:

    ServicesReportCrons = None

    ServicesDates = None

    ServicesReports = None

    ServicesCronjobs = None

    def __init__(self):

        self.initialize_services()

        self.initiliaze_services_interns() 

    def initialize_services(self):

        self.ServicesReportCrons = ServicesReportCrons.ServicesReportCrons()

        self.ServicesDates = ServicesDates.ServicesDate()  

        self.ServicesReports = ServicesReports.ServicesReports()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs() 

        return True 
    
    def initiliaze_services_interns(self):

        self.ServicesReportCrons.init_services_dates(self.ServicesDates)

        self.ServicesReportCrons.init_services_reports(self.ServicesReports)

        self.ServicesReportCrons.init_services_cronjobs(self.ServicesCronjobs)  

        return True
    
    def get_daily_report_crons(self):

        return self.ServicesReportCrons.get_daily_report_crons()

    def GetDailyReportCrons(self):

        return self.get_daily_report_crons()