import uuid

class EntitySendEntrys:

    config = None

    def __init__(self):

        self.init_config()

    def init_config(self):

        self.config = {
            'condition':1
        }

        return True

    def get_config(self, key):

        return self.config.get(key, None)

    def generate_id(self):

        return uuid.uuid4().hex