from decouple import config

class EntityApi():

    api_key = None

    condition = None

    api_description = None

    def __init__(self):

        self.init_api_key()

        self.init_condition()

        self.init_api_description()

    def init_api_description(self):

        self.api_description = config("API_DESCRIPTION")

    def get_api_description(self):

        return self.api_description

    def init_api_key(self):

        self.api_key = config("API")

    def init_condition(self):

        self.condition = config("CONDITION")

    def get_condition(self):

        return self.condition

    def get_api_key(self):

        return self.api_key

