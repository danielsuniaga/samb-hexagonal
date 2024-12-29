import uuid

class EntityCronjobs():
    
    def generate_cronjobs_id(self):

        return uuid.uuid4().hex