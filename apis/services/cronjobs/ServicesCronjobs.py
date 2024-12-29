import apis.entities.cronjobs.EntityCronjobs as EntityCronjobs

class ServicesCronjobs():

    entity = None

    def __init__(self):

        self.entity = EntityCronjobs.EntityCronjobs()

    def generate_cronjobs_id(self):

        return self.entity.generate_cronjobs_id()