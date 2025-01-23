import apis.entities.reportsentrys.EntityReportEntrys as EntityReportEntrys

class ServicesReportEntrys():

    entity = None

    ServicesReports = None

    def __init__(self):

        self.entity = EntityReportEntrys.EntityReportEntrys()

    def init_services_reports(self, value):

        self.ServicesReports = value

        return True
    
    def get_types_reports_daily(self):

        return self.entity.get_types_reports_daily()
    
    def add_persistence_daily_reports_entrys(self):

        type_reports = self.get_types_reports_daily()

        return self.ServicesReports.add_persistence(type_reports)

    def get_daily_report_entrys(self):
        
        return True