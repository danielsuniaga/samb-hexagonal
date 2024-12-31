from decouple import config

import uuid

class EntityCronjobs():

    condition = None

    id_api = None

    id_financial_asset = None

    default_execute = None

    def __init__(self):

        self.init_condition()

        self.init_id_api()

        self.init_id_financial_asset()

        self.init_default_execute()

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

        self.id_api = config("ID_API")

        return True
    
    def get_id_api(self):

        return self.id_api

    def init_condition(self):

        self.condition = config("CONDITION")

        return True
    
    def get_condition(self):

        return self.condition
    
    def generate_cronjobs_id(self):

        return uuid.uuid4().hex