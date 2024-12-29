from decouple import config

class EntityApi():

    api_key = None

    def __init__(self):

        self.init_api_key()

    def init_api_key(self):

        self.api_key = config("API")

    def get_api_key(self):

        return self.api_key

