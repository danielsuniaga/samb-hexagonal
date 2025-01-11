import apis.repositories.entrysresults.RepositoryEntrysResults as RepositoryEntrysResults
import apis.entities.entrysresults.EntityEntrysResults as EntityEntrysResults

class ServicesEntrysResults():

    repository = None

    entity = None

    def __init__(self):

        self.repository = RepositoryEntrysResults.RepositoryEntrysResults()

        self.entity = EntityEntrysResults.EntityEntrysResults()

    def get_sums_entrys_date_repository(self,date): 

        return self.repository.get_sums_entrys_date(date)
    
    def init_data_get_sums_entrys_date(self,result):

        return float(result['data'])

    def get_sums_entrys_date(self,date):

        result = self.get_sums_entrys_date_repository(date)

        return self.init_data_get_sums_entrys_date(result)
    
    def generate_id(self):

        return self.entity.generate_id()
    
    def init_data_add_persistence(self,data):

        return {
            'id_entry_result':self.generate_id(),
            'result_entry':'data',
            'current_date':'data',
            'condition':'data',
            'id_entry':'data'
        }
    
    def add_persistence_repository(self,data):

        return True
    
    def add_persistence(self,data):

        data_persistence = self.init_data_add_persistence(data)

        return self.add_persistence_repository(data_persistence)