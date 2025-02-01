import apis.services.datasets.ServicesDatasets as ServicesDatasets
import apis.services.models.ServicesModels as ServicesModels
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.indicators.ServicesIndicators as ServicesIndicators
import apis.services.metricsevaluationsmodels.ServicesMetricsEvaluationsModels as ServicesMetricsEvaluationsModels
import apis.services.dates.ServicesDates as ServicesDates
import apis.services.telegram.ServicesTelegram as ServicesTelegram

class ControllerAddModels():

    ServicesDatasets = None

    ServicesModels = None

    ServicesEntrys = None

    ServicesIndicators = None

    ServicesMetricsEvaluationsModels = None

    ServicesDates = None

    ServicesTelegram = None

    def __init__(self):

        self.initialize_services()

        self.initialize_services_interns()

    def initialize_services(self):  
        
        self.ServicesDatasets = ServicesDatasets.ServicesDatasets()

        self.ServicesModels = ServicesModels.ServicesModels()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()

        self.ServicesMetricsEvaluationsModels = ServicesMetricsEvaluationsModels.ServicesMetricsEvaluationsModels()

        self.ServicesDates = ServicesDates.ServicesDate()  

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()

        return True
    
    def initialize_services_interns(self):

        self.ServicesDatasets.init_services_entrys(self.ServicesEntrys)

        self.ServicesDatasets.init_services_indicators(self.ServicesIndicators)

        self.ServicesModels.init_services_datasets(self.ServicesDatasets)

        self.ServicesMetricsEvaluationsModels.init_services_dates(self.ServicesDates)

        return True
    
    def init_services_datasets(self):

        return [
            lambda: self.ServicesModels.get_active_model(),
            lambda: self.ServicesDatasets.add_dataset(),
            lambda: self.check_directory_ml()
        ]
    
    def check_directory(self, directory):
        
        return self.ServicesDatasets.check_directory(directory)
    
    def get_directory_general_ml(self):

        return self.ServicesModels.get_directory_general()
    
    def check_directory_ml(self):

        path = self.get_directory_general_ml()

        return self.check_directory(path)
    
    def generate_training_model(self):

        return self.ServicesModels.generate_training_model()
    
    def add_metrics_evaluations_models(self,data):

        return self.ServicesMetricsEvaluationsModels.add_metrics_evaluations_models(data)
    
    def generate_message_reports(self,data):

        return self.ServicesModels.generate_message_reports(data)
    
    def send_reports(self,data):

        message = self.generate_message_reports(data)

        print(message)

        return self.ServicesTelegram.send_message_report(message)

    def AddModels(self):

        servicios_a_verificar = self.init_services_datasets()

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado:
                
                return False
            
        models = self.generate_training_model()

        self.add_metrics_evaluations_models(models)

        return self.send_reports(models)