import apis.repositories.entrysresults.RepositoryEntrysResults as RepositoryEntrysResults
import apis.entities.entrysresults.EntityEntrysResults as EntityEntrysResults
import logging
import time
import os

logger = logging.getLogger('apis.services.entrysresults')

class ServicesEntrysResults():

    repository = None

    entity = None

    def __init__(self):

        self.repository = RepositoryEntrysResults.RepositoryEntrysResults()

        self.entity = EntityEntrysResults.EntityEntrysResults()

    def get_project_name(self):

        return self.entity.get_project_name()

    def get_condition(self):

        return self.entity.get_condition()

    def get_sums_entrys_date_repository(self,date,id_methodology): 

        return self.repository.get_sums_entrys_date(date,id_methodology)
    
    def init_data_get_sums_entrys_date(self,result):

        return float(result['data'])

    def get_sums_entrys_date(self,date,id_methodology):
        start_time = time.time()

        result = self.get_sums_entrys_date_repository(date,id_methodology)
        
        # Logging
        if result['status']:
            query_time = (time.time() - start_time) * 1000
            logger.info(
                f"💰 MONETARY FILTER | "
                f"Project: {self.get_project_name()} | "
                f"Method: get_sums_entrys_date | "
                f"Date: {date} | "
                f"Methodology: {id_methodology} | "
                f"Balance: ${result['data']:.2f} | "
                f"Query Time: {query_time:.2f}ms"
            )
        else:
            query_time = (time.time() - start_time) * 1000
            logger.error(
                f"❌ MONETARY FILTER ERROR | "
                f"Project: {self.get_project_name()} | "
                f"Method: get_sums_entrys_date | "
                f"Date: {date} | "
                f"Methodology: {id_methodology} | "
                f"Error: {result['msj']} | "
                f"Time: {query_time:.2f}ms"
            )

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
    
    def get_entrys_results_curdate_repository_complete(self):

        return self.repository.get_entrys_results_curdate_complete()
    
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
        start_time = time.time()

        result = self.get_entrys_results_curdate_repository(id_methodology)
        
        # Logging
        if result['status']:
            query_time = (time.time() - start_time) * 1000
            methodology_id = id_methodology[0] if isinstance(id_methodology, tuple) else id_methodology
            for row in result['result']:
                logger.info(
                    f"💰 MONETARY FILTER | "
                    f"Project: {self.get_project_name()} | "
                    f"Method: get_data_entrys_results_curdate | "
                    f"Methodology: {methodology_id} | "
                    f"Account: {row['type_account']} | "
                    f"Total: {row['total']} | "
                    f"Positive: {row['positive_count']} | "
                    f"Negative: {row['negative_count']} | "
                    f"Balance: ${row['result']:.2f} | "
                    f"Query Time: {query_time:.2f}ms"
                )
        else:
            query_time = (time.time() - start_time) * 1000
            methodology_id = id_methodology[0] if isinstance(id_methodology, tuple) else id_methodology
            logger.error(
                f"❌ MONETARY FILTER ERROR | "
                f"Project: {self.get_project_name()} | "
                f"Method: get_data_entrys_results_curdate | "
                f"Methodology: {methodology_id} | "
                f"Error: {result['message']} | "
                f"Time: {query_time:.2f}ms"
            )

        return self.init_data_get_entrys_results(result,data)
    
    def get_data_entrys_results_curdate_complete(self,data):
        start_time = time.time()

        result = self.get_entrys_results_curdate_repository_complete()
        
        # Logging
        if result['status']:
            query_time = (time.time() - start_time) * 1000
            for row in result['result']:
                logger.info(
                    f"💰 MONETARY FILTER | "
                    f"Project: {self.get_project_name()} | "
                    f"Method: get_data_entrys_results_curdate_complete | "
                    f"Account: {row['type_account']} | "
                    f"Total: {row['total']} | "
                    f"Positive: {row['positive_count']} | "
                    f"Negative: {row['negative_count']} | "
                    f"Balance: ${row['result']:.2f} | "
                    f"Query Time: {query_time:.2f}ms"
                )
        else:
            query_time = (time.time() - start_time) * 1000
            logger.error(
                f"❌ MONETARY FILTER ERROR | "
                f"Project: {self.get_project_name()} | "
                f"Method: get_data_entrys_results_curdate_complete | "
                f"Error: {result['message']} | "
                f"Time: {query_time:.2f}ms"
            )

        return self.init_data_get_entrys_results(result,data)   
    
    def get_entrys_results_total_repository(self,id_methodology):

        return self.repository.get_entrys_results_total(id_methodology)
    
    def get_entrys_results_total_repository_complete(self):

        return self.repository.get_entrys_results_total_complete()   
    
    def get_data_entrys_results_total(self,data,id_methodology):   

        result = self.get_entrys_results_total_repository(id_methodology)

        return self.init_data_get_entrys_results(result,data)
    
    def get_data_entrys_results_total_complete(self,data):   

        result = self.get_entrys_results_total_repository_complete()

        return self.init_data_get_entrys_results(result,data)    
    
    def get_entrys_results_nom_repository(self,day,id_methodology):

        return self.repository.get_entrys_results_nom(day,id_methodology)
    
    def get_entrys_results_nom_repository_complete(self,day):

        return self.repository.get_entrys_results_nom_complete(day)
    
    def get_data_entrys_results_nom(self,data,id_methodology):

        result = self.get_entrys_results_nom_repository(data['IND'],id_methodology)

        return self.init_data_get_entrys_results(result,data)
    
    def get_data_entrys_results_nom_complete(self,data):

        result = self.get_entrys_results_nom_repository_complete(data['IND'])

        return self.init_data_get_entrys_results(result,data)