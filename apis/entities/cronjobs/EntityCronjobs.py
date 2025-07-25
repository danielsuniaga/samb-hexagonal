from decouple import config

import uuid

class EntityCronjobs():

    condition = None

    id_api = None

    id_financial_asset = None

    default_execute = None

    id_cronjobs = None

    success_condition = None

    def __init__(self):

        self.init_condition()

        self.init_id_api()

        self.init_id_financial_asset()

        self.init_default_execute()

        self.init_success_condition()

    def init_success_condition(self):

        self.success_condition = config("SUCCESS_CONDITION")

        return True 
    
    def get_success_condition(self):
        
        return self.success_condition

    def set_id_cronjobs(self,id_cronjobs):

        self.id_cronjobs = id_cronjobs

        return True
    
    def get_id_cronjobs(self):

        return self.id_cronjobs

    def init_default_execute(self):

        self.default_execute = config("DEFAULT_EXECUTE")

        return True
    
    def get_default_execute(self):

        return self.default_execute

    def init_id_financial_asset(self):

        self.id_financial_asset = config("ID_FINANCIAL_ASSET")

        return True

    def get_id_financial_asset(self):

        return self.id_financial_asset
    
    def init_id_api(self):

        self.id_api = {
            'trends':config("ID_API"),
            'wma':config("ID_API_WMA"),
            'trends_expansive':config("ID_API_TRENDS_EXPANSIVE"),
            'trends_minus':config("ID_API_TRENDS_MINUS")
        }

        return True
    
    def get_id_api_trends(self):

        return self.get_id_api_key('trends')
    
    def get_id_api_trends_expansive(self):

        return self.get_id_api_key('trends_expansive')
    
    def get_id_api_trends_minus(self):

        return self.get_id_api_key('trends_minus')

    def get_id_api_wma(self):

        return self.get_id_api_key('wma')   
    
    def get_id_api_key(self,key):

        return self.id_api[key]

    def init_condition(self):

        self.condition = config("CONDITION")

        return True
    
    def get_condition(self):

        return self.condition
    
    def generate_cronjobs_id(self):

        return uuid.uuid4().hex