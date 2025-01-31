import apis.services.datasets.ServicesDatasets as ServicesDatasets
import apis.services.models.ServicesModels as ServicesModels
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.indicators.ServicesIndicators as ServicesIndicators

class ControllerAddModels():

    ServicesDatasets = None

    ServicesModels = None

    ServicesEntrys = None

    ServicesIndicators = None

    def __init__(self):

        self.initialize_services()

        self.initialize_services_interns()

    def initialize_services(self):  
        
        self.ServicesDatasets = ServicesDatasets.ServicesDatasets()

        self.ServicesModels = ServicesModels.ServicesModels()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()

        return True
    
    def initialize_services_interns(self):

        self.ServicesDatasets.init_services_entrys(self.ServicesEntrys)

        self.ServicesDatasets.init_services_indicators(self.ServicesIndicators)

        self.ServicesModels.init_services_datasets(self.ServicesDatasets)

        return True
    
    def init_services_datasets(self):

        return [
            lambda: self.ServicesModels.get_active_model(),
            lambda: self.ServicesDatasets.add_dataset()
        ]
    
    def generate_training_model(self):

        return self.ServicesModels.generate_training_model()

    def AddModels(self):

        servicios_a_verificar = self.init_services_datasets()

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado:
                
                return False

        return self.generate_training_model()