from decouple import config

class EntityReportsCrons():

    types_reports = None

    def __init__(self):

        self.init_types_reports()

        
    def init_types_reports(self):

        self.types_reports = {
            "daily": config("REPORTS_CRON_DAILY"),
        }

        return True
    
    def get_types_reports_daily(self):

        return self.types_reports['daily']

