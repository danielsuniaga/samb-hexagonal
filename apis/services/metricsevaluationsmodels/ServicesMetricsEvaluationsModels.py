import apis.entities.metricsevaluationsmodels.EntityMetricsEvaluationsModels as EntityMetricsEvaluationsModels

import apis.repositories.metricsevaluationsmodels.RepositoryMetricsEvaluationsModels as RepositoryMetricsEvaluationsModels

class ServicesMetricsEvaluationsModels:

    entity = None

    repository = None

    ServicesDates = None

    def __init__(self):

        self.entity = EntityMetricsEvaluationsModels.EntityMetricsEvaluationsModels()   

        self.repository = RepositoryMetricsEvaluationsModels.RepositoryMetricsEvaluationsModels()

    def init_services_dates(self,value):
        
        self.ServicesDates = value

        return True

    def generate_id(self):

        return self.entity.generate_id()
    
    def get_config_condition(self):

        return self.entity.get_config_condition()

    def add_metrics_evaluations_models_repository(self, data):

        for data in data:

            result  = self.repository.add(data)

            if not result['status']:

                return result

        return True
    
    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()

    def init_data_add_metrics_evaluations_models(self, data):

        result = []

        date = self.get_current_date_hour()

        for model, metrics in data.items():

            model_data = {
                'id': self.generate_id(),
                'id_models': metrics['id'],
                'accuracy': round(metrics['accuracy'], 3),
                'precisions': round(metrics['precision'], 3),
                'recall': round(metrics['recall'], 3),
                'f1_score': round(metrics['f1_score'], 3),
                'registration_date': date,
                'update_date': date,
                'state': self.get_config_condition()
            }

            result.append(model_data)

        return result

    def add_metrics_evaluations_models(self, data):

        data_persistence = self.init_data_add_metrics_evaluations_models(data)

        return self.add_metrics_evaluations_models_repository(data_persistence)