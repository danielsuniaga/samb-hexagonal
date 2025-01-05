import apis.repositories.entrysresults.RepositoryEntrysResults as RepositoryEntrysResults

class ServicesEntrysResults():

    repository = None

    def __init__(self):

        self.repository = RepositoryEntrysResults.RepositoryEntrysResults()

    def get_sums_entrys_date_repository(self,date): 

        return self.repository.get_sums_entrys_date(date)
    
    def init_data_get_sums_entrys_date(self,result):

        return float(result['data'])

    def get_sums_entrys_date(self,date):

        result = self.get_sums_entrys_date_repository(date)

        return self.init_data_get_sums_entrys_date(result)