import apis.services.reportentrys.ServicesReportEntrys as ServicesReportEntrys
import apis.services.reports.ServicesReports as ServicesReports 

class ControllerGetDailyReportEntrys:

    ServicesReportEntrys = None

    ServicesReports = None

    def __init__(self):

        self.initialize_services()

    def initialize_services(self):
        
        self.ServicesReportEntrys = ServicesReportEntrys.ServicesReportEntrys() 

        self.ServicesReports = ServicesReports.ServicesReports()

        return True

    def initialize_services_interns(self):

        self.ServicesReportEntrys.init_services_reports(self.ServicesReports)

        return True

    def GetDailyReportEntrys(self):

        return self.ServicesReportEntrys.get_daily_report_entrys()