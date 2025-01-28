import apis.entities.generalmodellogisticregression.EntityGeneralModelLogisticRegression as EntityGeneralModelLogisticRegression

class ServicesGeneralModelLogisticRegression: 

    entity = None

    def __init__(self):
        
        self.entity = EntityGeneralModelLogisticRegression.EntityGeneralModelLogisticRegression()

    def get_config_active(self):
        
        return self.entity.get_config_active()

    def get_active_model(self):

        if not self.get_config_active():
            
            return False
        
        return True