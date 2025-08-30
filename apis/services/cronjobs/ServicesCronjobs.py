import apis.entities.cronjobs.EntityCronjobs as EntityCronjobs

import apis.repositories.cronjobs.RepositoryCronjobs as RepositoryCronjobs

class ServicesCronjobs():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityCronjobs.EntityCronjobs()

        self.repository = RepositoryCronjobs.RepositoryCronjobs()

    def add_repository(self,data):

        return self.repository.add(data)
    
    def set_id_cronjobs(self,id_cronjobs):

        return self.entity.set_id_cronjobs(id_cronjobs)

    def generate_cronjobs_id(self):

        result =  self.entity.generate_cronjobs_id()

        self.set_id_cronjobs(result)

        return result
    
    def get_id_cronjobs(self):

        return self.entity.get_id_cronjobs()
    
    def get_condition(self):

        return self.entity.get_condition()
    
    def get_id_api_trends(self):

        return self.entity.get_id_api_trends()

    def get_id_api_trends_ml(self):

        return self.entity.get_id_api_trends_ml()

    def get_id_api_trends_minus_ml(self):

        return self.entity.get_id_api_trends_minus_ml()

    def get_id_api_trends_expansive(self):

        return self.entity.get_id_api_trends_expansive()
    
    def get_id_api_wma(self):

        return self.entity.get_id_api_wma()
    
    def get_id_api_wma_ml(self):

        return self.entity.get_id_api_wma_ml()
    
    def get_id_api_trends_minus(self):

        return self.entity.get_id_api_trends_minus()
    
    def get_id_api_envolvent(self):

        return self.entity.get_id_api_envolvent()
    
    def get_id_financial_asset(self):

        return self.entity.get_id_financial_asset()
    
    def get_default_execute(self):

        return self.entity.get_default_execute()
    
    def init_add_trends_expansive_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_expansive(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_minus_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_minus_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_wma_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_wma(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }

    def init_add_wma_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_wma_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    def add_trends_ml(self,id_cronjobs,date):

        data = self.init_add_trends_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_minus_ml(self,id_cronjobs,date):

        data = self.init_add_trends_minus_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends(self,id_cronjobs,date):

        data = self.init_add_trends_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_expansive(self,id_cronjobs,date):

        data = self.init_add_trends_expansive_repository(id_cronjobs,date)

        return self.add_repository(data)

    def init_data_add_trends_minus_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_minus(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add_trends_minus(self,id_cronjobs,date):

        data = self.init_data_add_trends_minus_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def init_data_add_envolvent_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_envolvent(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add_envolvent(self,id_cronjobs,date):

        data = self.init_data_add_envolvent_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_wma(self,id_cronjobs,date):

        data = self.init_add_wma_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_wma_ml(self,id_cronjobs,date):

        data = self.init_add_wma_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def get_success_condition(self):

        return self.entity.get_success_condition()
    
    def init_data_set_ejecution(self,date,time_execution,id_cronjobs):

        return {
            'success_condition':self.get_success_condition(),
            'end_date':date,
            'execute_time':time_execution,
            'id_cronjobs':id_cronjobs
        }
    
    def set_ejecution_repository(self,data):

        return self.repository.set(data)
    
    def set_ejecution(self,date,time_execution,id_cronjobs):

        data_persistence = self.init_data_set_ejecution(date,time_execution,id_cronjobs)

        return self.set_ejecution_repository(data_persistence)
    
    def init_data_get_data_cronjobs_curdate(self,data,result):

        if result['status']:

            data['data']['quantities'] = result['result']['quantities']

            data['data']['max_durations'] = result['result']['max_durations']

        return data
    
    def get_data_cronjobs_curdate(self,data):

        result = self.repository.get_data_cronjobs_curdate(data)

        return self.init_data_get_data_cronjobs_curdate(data,result)