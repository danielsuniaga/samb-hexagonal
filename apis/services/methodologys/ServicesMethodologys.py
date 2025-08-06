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

        return self.init_data_result_get_methodologys(result)
    
    def init_data_get_methodology_description_number_by_id(self, id_methodology):

        return {
            'id_methodology': id_methodology
        }
    
    def get_methodology_description_number_by_id_repository(self, data):

        return self.repository.get_methodology_description_number_by_id(data)
    
    def init_result_get_methodology_description_number_by_id(self, result):

        if result.get('status') and result.get('data'):
            return result['data'][0].get('description_number')
        return None
    
    def get_methodology_description_number_by_id(self, id_methodology):

        data_persistence = self.init_data_get_methodology_description_number_by_id(id_methodology)  

        result = self.get_methodology_description_number_by_id_repository(data_persistence)

        return self.init_result_get_methodology_description_number_by_id(result)