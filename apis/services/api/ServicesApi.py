import apis.entities.api.EntityApi as EntityApi

import apis.repositories.api.RepositoryApi as RepositoryApi
class ServicesApi():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityApi.EntityApi()

        self.repository = RepositoryApi.RepositoryApi()

        self.init_methods_internal()

    def init_methods_internal(self):

        self.get_apis_entity()

    def init_data_get_apis_repository(self):

        return {
            'condition':self.get_condition()
        }

    def get_apis_repository(self):

        data = self.init_data_get_apis_repository()

        return self.repository.get_apis(data)
    
    def init_data_get_apis_entity(self, result):

        if result.get('status') and 'data' in result:

            return [{'id': item['id'], 'description': item['description']} for item in result['data']]
        
        return []
    
    def set_apis_entity(self, result):

        self.entity.set_apis(result)

        return True

    def get_apis_entity(self):

        result = self.get_apis_repository()

        data_entity = self.init_data_get_apis_entity(result)

        return self.entity.set_apis_name(data_entity)

    def get_api_description(self):

        return self.entity.get_api_description()

    def get_condition(self):

        return self.entity.get_condition()
    
    def init_data_get_api_result(self):

        return {
            'api_description':self.get_api_description(),
            'condition':self.get_condition()
        }
    
    def get(self,data):

        return self.repository.get(data)
    
    def get_api_result(self):

        data = self.init_data_get_api_result()

        return self.get(data)
    
    def get_apis_name_trends(self):

        return self.entity.get_apis_name_trends()
    
    def get_apis_name_trends_recent(self):

        return self.entity.get_apis_name_trends_recent()

    def get_apis_name_trends_ml(self):

        return self.entity.get_apis_name_trends_ml()

    def get_apis_name_trends_minus_ml(self):

        return self.entity.get_apis_name_trends_minus_ml()

    def get_apis_name_wma(self):
            
        return self.entity.get_apis_name_wma()
    
    def get_apis_name_wma_recent(self):
            
        return self.entity.get_apis_name_wma_recent()
    
    def get_apis_name_wma_recent_ml(self):
            
        return self.entity.get_apis_name_wma_recent_ml()
    
    def get_apis_name_wma_ml(self):

        return self.entity.get_apis_name_wma_ml()

    def get_apis_name_trends_expansive(self):
                
        return self.entity.get_apis_name_trends_expansive()
    
    def get_apis_name_trends_expansive_ml(self):
                
        return self.entity.get_apis_name_trends_expansive_ml()
    
    def get_apis_name_trends_expansive_recent(self):
                
        return self.entity.get_apis_name_trends_expansive_recent()
    
    def get_apis_name_trends_minus(self):

        return self.entity.get_apis_name_trends_minus()

    def get_apis_name_trends_minus_recent(self):

        return self.entity.get_apis_name_trends_minus_recent()

    def get_apis_name_envolvent(self):

        return self.entity.get_apis_name_envolvent()
    
    def get_apis_name_envolvent_ml(self):

        return self.entity.get_apis_name_envolvent_ml()

    def get_apis_name_pinbar(self):

        return self.entity.get_apis_name_pinbar()

    def get_apis_name_pinbar_ml(self):

        return self.entity.get_apis_name_pinbar_ml()

    def get_apis_name_endpoints(self):
                
        return self.entity.get_apis_name_endpoints()

    def get_api_key(self,request):

        # return self.repository.get_api_key(self.entity.get_api_key(), request,self.get_condition())

        return self.api.get_api_key(self.api_key,request.headers.get(self.api_key)) if self.api_key in request.headers else {'status':False,'msj': "No se envio la key"}