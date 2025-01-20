import apis.repositories.entrysresults.RepositoryEntrysResults as RepositoryEntrysResults
import apis.entities.entrysresults.EntityEntrysResults as EntityEntrysResults

class ServicesEntrysResults():

    repository = None

    entity = None

    def __init__(self):

        self.repository = RepositoryEntrysResults.RepositoryEntrysResults()

        self.entity = EntityEntrysResults.EntityEntrysResults()

    def get_condition(self):

        return self.entity.get_condition()

    def get_sums_entrys_date_repository(self,date): 

        return self.repository.get_sums_entrys_date(date)
    
    def init_data_get_sums_entrys_date(self,result):

        return float(result['data'])

    def get_sums_entrys_date(self,date):

        result = self.get_sums_entrys_date_repository(date)

        return self.init_data_get_sums_entrys_date(result)
    
    def generate_id(self):

        return self.entity.generate_id()
    
    def get_data_result_entry_add_persistence(self,data):

        return self.entity.get_data_result_entry_add_persistence(data)
    
    def init_data_add_persistence(self,data,data_indicators):

        return {
            'id_entry_result':self.generate_id(),
            'result_entry':self.get_data_result_entry_add_persistence(data),
            'current_date':data['current_date'],
            'condition':self.get_condition(),
            'id_entry':data_indicators['data_entry']['id_entry']
        }
    
    def add_persistence_repository(self,data):

        return self.repository.add(data)
    
    def add_persistence(self,data,data_indicators):

        data_persistence = self.init_data_add_persistence(data,data_indicators)

        return self.add_persistence_repository(data_persistence)