from decouple import config

class EntityShedule():

    shedule_permission = None

    condition = None

    def __init__(self):

        self.init_shedule_permission()

        self.init_condition()

    def init_condition(self):

        self.condition = config("CONDITION")

    def get_condition(self):

        return self.condition

    def init_shedule_permission(self):

        self.shedule_permission = config("SHEDULE_PERMISSION")

    def get_shedule_permission(self):

        return self.shedule_permission