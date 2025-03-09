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

    def get_sums_entrys_date_repository(self,date,id_methodology): 

        return self.repository.get_sums_entrys_date(date,id_methodology)
    
    def init_data_get_sums_entrys_date(self,result):

        return float(result['data'])

    def get_sums_entrys_date(self,date,id_methodology):

        result = self.get_sums_entrys_date_repository(date,id_methodology)

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
    
    def get_entrys_results_curdate_repository(self,id_methodology):

        return self.repository.get_entrys_results_curdate(id_methodology)
    
    def init_data_get_entrys_results(self, result, data):

        if not result['status']:
            return False
        
        account_types = {'PRACTICE': 'D', 'REAL': 'R'}
        
        for item in result['result']:
            account_type = account_types.get(item['type_account'])
            if account_type:
                data[account_type]['USD'] = float(item['result'])
                data[account_type]['ENT'] = item['quantities']
                data['E']['DEM'] += item['total'] if account_type == 'D' else 0
                data['E']['REA'] += item['total'] if account_type == 'R' else 0
        
        return data
    
    def get_data_entrys_results_curdate(self,data,id_methodology):

        result = self.get_entrys_results_curdate_repository(id_methodology)

        return self.init_data_get_entrys_results(result,data)
    
    def get_entrys_results_total_repository(self,id_methodology):

        return self.repository.get_entrys_results_total(id_methodology)
    
    def get_data_entrys_results_total(self,data,id_methodology):   

        result = self.get_entrys_results_total_repository(id_methodology)

        return self.init_data_get_entrys_results(result,data)
    
    def get_entrys_results_nom_repository(self,day,id_methodology):

        return self.repository.get_entrys_results_nom(day,id_methodology)
    
    def get_data_entrys_results_nom(self,data,id_methodology):

        result = self.get_entrys_results_nom_repository(data['IND'],id_methodology)

        return self.init_data_get_entrys_results(result,data)