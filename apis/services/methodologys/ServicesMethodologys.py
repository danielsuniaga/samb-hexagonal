import apis.entities.methodologys.EntityMethodologys as EntityMethodologys
import apis.repositories.methodologys.RepositoryMethodologys as RepositoryMethodologys


class ServicesMethodologys:

    repository = None

    entity = None

    def __init__(self):

        self.entity = EntityMethodologys.EntityMethodologys()   

        self.repository = RepositoryMethodologys.RepositoryMethodologys()

    def get_condition_success(self):
        
        return self.entity.get_config_condition_success()

    def get_methodologys_repository(self,data):

        return self.repository.get_methodologys(data)
    
    def init_data_get_methodologys(self):

        return {
            'condition_success': self.get_condition_success()
        }
    
    def init_data_result_get_methodologys(self, result):

        return result['data']   

    def get_methodologys(self):

        data = self.init_data_get_methodologys()

        result = self.get_methodologys_repository(data)

        print("result:",self.init_data_result_get_methodologys(result))

        return True