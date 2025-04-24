import apis.services.reportentrys.ServicesReportEntrys as ServicesReportEntrys
import apis.services.reports.ServicesReports as ServicesReports 
import apis.services.dates.ServicesDates as ServicesDate
import apis.services.telegram.ServicesTelegram as ServicesTelegram
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults
import apis.services.methodologys.ServicesMethodologys as ServicesMethodologys
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays

class ControllerGetDailyReportEntrys:

    ServicesReportEntrys = None

    ServicesReports = None

    ServicesDates = None

    ServicesTelegram = None

    ServicesEntrysResults = None

    ServicesMethodologys = None

    ServicesManagerDays = None

    def __init__(self):

        self.initialize_services()

        self.initialize_services_interns()

    def initialize_services(self):
        
        self.ServicesReportEntrys = ServicesReportEntrys.ServicesReportEntrys() 

        self.ServicesReports = ServicesReports.ServicesReports()

        self.ServicesDates = ServicesDate.ServicesDate()  

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram() 

        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()

        self.ServicesMethodologys = ServicesMethodologys.ServicesMethodologys()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        return True

    def initialize_services_interns(self):

        self.ServicesReportEntrys.init_services_reports(self.ServicesReports)

        self.ServicesReportEntrys.init_services_dates(self.ServicesDates)

        self.ServicesReportEntrys.init_services_telegram(self.ServicesTelegram)

        self.ServicesReportEntrys.init_services_reportsentrys(self.ServicesEntrysResults)

        self.ServicesReportEntrys.init_services_methodologys(self.ServicesMethodologys)

        self.ServicesReportEntrys.init_services_manager_days(self.ServicesManagerDays)

        return True

    def GetDailyReportEntrys(self):

        return self.ServicesReportEntrys.get_daily_report_entrys()