import apis.entities.api.EntityApi as EntityApi

import apis.repositories.api.RepositoryApi as RepositoryApi
class ServicesApi():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityApi.EntityApi()

        self.repository = RepositoryApi.RepositoryApi()

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

    def get_api_key(self,request):

        # return self.repository.get_api_key(self.entity.get_api_key(), request,self.get_condition())

        return self.api.get_api_key(self.api_key,request.headers.get(self.api_key)) if self.api_key in request.headers else {'status':False,'msj': "No se envio la key"}