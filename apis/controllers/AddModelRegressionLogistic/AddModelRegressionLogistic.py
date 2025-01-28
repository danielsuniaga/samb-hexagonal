import apis.services.datasets.ServicesDatasets as ServicesDatasets
import apis.services.generalmodellosgisticregression.ServicesGeneralModelLogisticRegression as ServicesGeneralModelLogisticRegression
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.indicators.ServicesIndicators as ServicesIndicators

class ControllerAddModelRegressionLogistic():

    ServicesDatasets = None

    ServicesGeneralModelLogisticRegression = None

    ServicesEntrys = None

    ServicesIndicators = None

    def __init__(self):

        self.initialize_services()

        self.initialize_services_interns()

    def initialize_services(self):  
        
        self.ServicesDatasets = ServicesDatasets.ServicesDatasets()

        self.ServicesGeneralModelLogisticRegression = ServicesGeneralModelLogisticRegression.ServicesGeneralModelLogisticRegression()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()

        return True
    
    def initialize_services_interns(self):

        self.ServicesDatasets.init_services_entrys(self.ServicesEntrys)

        self.ServicesDatasets.init_services_indicators(self.ServicesIndicators)

        return True

    def AddModelRegressionLogistic(self):

        result = self.ServicesGeneralModelLogisticRegression.get_active_model()

        if not result:

            return False
        
        result = self.ServicesDatasets.add_dataset()
        
        return result