from decouple import config

class EntityReportEntrys():

    types_reports = None

    data_reports = None

    def __init__(self):

        self.init_types_reports()

        self.init_data_reports()

    def init_data_reports(self):

        self.data_reports = [
            {
                'name':'CUR',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'SUN',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'MON',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'TUE',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'WED',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'THU',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'FRI',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'SAT',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            },
            {
                'name':'TOT',
                'data':{
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    }
                }
            }
        ]

        return True
    
    def get_data_reports(self):

        return self.data_reports

    def init_types_reports(self):

        self.types_reports = {
            "daily": config("REPORTS_ENTRYS_DAILY"),
        }

        return True
    
    def get_types_reports_daily(self):
        
        return self.types_reports['daily']
    
    def generate_message(self):

        message = " DAILY REPORTS ("+config("PROJECT_NAME")+")\n"

        days = ["CUR", "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN", "TOT"]

        report_lines = [f"{day}:{{R(0,0), D(0,0)}}" for day in days]

        max_length = max(len(line) for line in report_lines)

        centered_lines = [line.center(max_length) for line in report_lines]

        return message + "\n".join(centered_lines) + "\n"