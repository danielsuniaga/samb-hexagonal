import uuid

from decouple import config

class EntitySmtp():

    condition = None

    def __init__(self):

        self.init_condition()

    def init_condition(self):

        self.condition = config("CONDITION")

    def get_condition(self):

        return self.condition

    def generate_id(self):

        return uuid.uuid4().hex