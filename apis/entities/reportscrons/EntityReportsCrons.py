from decouple import config

class EntityReportsCrons():

    types_reports = None

    data_reports = None

    titles_reports = None

    def __init__(self):

        self.init_types_reports()

        self.init_data_reports()

        self.init_titles_reports()

    def init_titles_reports(self):

        self.titles_reports = {
            "daily": "DAILY REPORTS CRON(" + config("PROJECT_NAME") + ")",
        }

        return True
    
    def get_titles_reports_daily(self):

        return self.titles_reports['daily']

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
    
    def generate_message(self, data):

        message = self.get_titles_reports_daily() + "\n"

        for report in data:

            state = report['state']

            quantities = report['data']['quantities']

            max_durations = round(float(report['data']['max_durations']), 2)

            message += f"{state} : quantities({quantities}), max durations({max_durations})\n"

        return message

