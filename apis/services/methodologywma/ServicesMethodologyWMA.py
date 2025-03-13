import apis.entities.methodologywma.EntityMethodologyWMA as EntityMethodologyWMA

class ServicesMethodologyWMA:

    entity = None

    def __init__(self):

        self.entity = EntityMethodologyWMA.EntityMethodologyWMA()

    def get_id(self):
        
        return self.entity.get_id()