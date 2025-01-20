import apis.entities.events.EntityEvents as EntityEvents

class ServicesEvents():

    entity = None

    def __init__(self):

        self.entity = EntityEvents.EntityEvents()

    def set_events_field(self,field,value):

        return self.entity.set_events_field(field,value)
    
    def get_events(self):

        return self.entity.get_events()