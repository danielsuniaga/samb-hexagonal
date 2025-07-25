from decouple import config

class EntityReportEntrys():

    types_reports = None

    data_reports = None

    titles_reports = None

    message_params = None

    def __init__(self):

        self.init_types_reports()

        self.init_data_reports()

        self.init_titles_reports()

        self.init_message_params()

    def set_message_params(self, message):

        self.message_params = message

        return True
    
    def get_message_params(self):

        return self.message_params

    def init_message_params(self):

        self.message_params = "PARAMS\n"

        return True

    def init_titles_reports(self):

        self.titles_reports = {
            "daily": "DAILY REPORTS (" + config("PROJECT_NAME") + ")",
            "daily_complete_complement": config("REPORT_DAILY_COMPLETE_COMPLEMENT")
        }

        return True
    
    def get_titles_reports_daily(self):

        return self.titles_reports['daily']
    
    def get_titles_reports_daily_complete_complement(self):
            
        return self.titles_reports['daily_complete_complement']

    def init_data_reports(self):

        self.data_reports = [
            {
                'name':'CUR',
                'data':{
                    'IND':0,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'SUN',
                'data':{
                    'IND':1,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'MON',
                'data':{
                    'IND':2,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'TUE',
                'data':{
                    'IND':3,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'WED',
                'data':{
                    'IND':4,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'THU',
                'data':{
                    'IND':5,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'FRI',
                'data':{
                    'IND':6,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'SAT',
                'data':{
                    'IND':7,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
                    }
                }
            },
            {
                'name':'TOT',
                'data':{
                    'IND':8,
                    'R':{
                        'USD':0,
                        'ENT':0,
                    },
                    'D':{
                        'USD':0,
                        'ENT':0,
                    },
                    'E':{
                        'DEM':0,
                        'REA':0,
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

    def generate_message(self, data, name_methodology):

        message = self.get_titles_reports_daily()+" ("+name_methodology+") \n"

        report_lines = self.generate_report_lines(data)

        return message + self.get_message_params() +"\n".join(report_lines) + "\n"
    
    def generate_message_parameters(self, data):

        return "PARAMS: (Type: "+str(data['type'])+", Day: "+str(data['day_description'])+" Permission real: "+str(data['permision_real'])+", Profit: "+str(data['profit'])+", Loss: "+str(data['loss'])+", Money: "+str(data['money'])+", Obs:"+str(data['observations'])+") \n"

    def generate_report_lines(self, data):

        report_lines = []

        for entry in data:

            name = entry['name']

            r_usd = round(entry['data']['R']['USD'], 2)

            r_ent = entry['data']['R']['ENT']

            d_usd = round(entry['data']['D']['USD'], 2)

            d_ent = entry['data']['D']['ENT']

            e_dem = entry['data']['E']['DEM']

            e_rea = entry['data']['E']['REA']

            report_lines.append(f"{name}: R({r_usd},{r_ent}), D({d_usd},{d_ent}), E({e_dem},{e_rea})")

        return report_lines
