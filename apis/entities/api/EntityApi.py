from decouple import config

class EntityApi():

    api_key = None

    condition = None

    api_description = None

    apis_name = None

    apis_ids = None

    def __init__(self):

        self.init_api_key()

        self.init_condition()

        self.init_api_description()

        self.init_apis_ids()

    def init_apis_ids(self):

        self.apis_ids = {
            'trends':config("ID_API"),
            'wma':config("ID_API_WMA"),
            'trends_expansive':config("ID_API_TRENDS_EXPANSIVE"),
            'trends_minus':config("ID_API_TRENDS_MINUS"),
            'trends_ml':config("ID_API_TRENDS_ML"),
            'endpoinst':config("ID_API_ENDPOINT"),
        }

        return True
    
    def get_apis_name(self,id):
            
        if self.apis_name is not None:

            for api in self.apis_name:

                if api['id'] == id:

                    return api['description']

        return None
    
    def get_apis_ids(self,key):

        if self.apis_ids is not None:

            return self.apis_ids[key]

        return None
    
    def get_apis_name_trends(self):

        id = self.get_apis_ids('trends')

        return self.get_apis_name(id)
    
    def get_apis_name_trends_ml(self):

        id = self.get_apis_ids('trends_ml')

        return self.get_apis_name(id)
    
    def get_apis_name_wma(self):

        id = self.get_apis_ids('wma')

        return self.get_apis_name(id)
    
    def get_apis_name_trends_expansive(self):
            
        id = self.get_apis_ids('trends_expansive')

        return self.get_apis_name(id)
    
    def get_apis_name_trends_minus(self):

        id = self.get_apis_ids('trends_minus')

        return self.get_apis_name(id)
    
    def get_apis_name_endpoints(self):
            
        id = self.get_apis_ids('endpoinst')

        return self.get_apis_name(id)

    def set_apis_name(self, apis):

        self.apis_name = apis

        return True

    def init_api_description(self):

        self.api_description = config("API_DESCRIPTION")

    def get_api_description(self):

        return self.api_description

    def init_api_key(self):

        self.api_key = config("API")

    def init_condition(self):

        self.condition = config("CONDITION")

    def get_condition(self):

        return self.condition

    def get_api_key(self):

        return self.api_key

