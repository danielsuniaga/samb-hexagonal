from decouple import config

class EntityReportsCrons():

    types_reports = None

    data_reports = None

    def __init__(self):

        self.init_types_reports()

        self.init_data_reports()

    def get_data_reports(self):

        return self.data_reports
    
    def init_data_reports(self):

        self.data_reports = [
            {
            'state': '1',
            'data': {
                'quantities': 0,
                'max_durations': 0,
                }
            },
            {
            'state': '2',
            'data': {
                'quantities': 0,
                'max_durations': 0,
                }
            }
        ]

        return True

        
    def init_types_reports(self):

        self.types_reports = {
            "daily": config("REPORTS_CRON_DAILY"),
        }

        return True
    
    def get_types_reports_daily(self):

        return self.types_reports['daily']

