from decouple import config

class EntityMethodologyWMA:

    config = None

    def __init__(self):

        self.init_config()

    def init_config(self):

        self.config = {
            'name':config("NAME_METHODOLOGY_WMA"),
            'id':config("ID_METHODOLOGY_WMA")
        }

        return True
    
    def get_id(self):

        return self.config['id']  