from decouple import config
import uuid

class EntityManagerDays():

    money = None

    profit = None

    loss = None

    mode = None

    mode_env = None

    mode_real = None

    project_name = None

    def __init__(self):

        self.init_modes()
        self.init_project_name()

    def generate_uuid(self):

        return str(uuid.uuid4())[:8]

    def init_project_name(self):

        self.project_name = config("PROJECT_NAME")

        return True
    
    def get_project_name(self):

        return self.project_name
    
    def init_modes(self):

        self.mode = config("MODE")

        self.mode_env = config("MODE")

        self.mode_real = config("MODE_REAL")

        return True

    def get_mode(self):

        return self.mode
    
    def get_money(self):

        return self.money
    
    def get_profit(self):

        return self.profit
    
    def get_loss(self):

        return self.loss

    def set_money(self,value):

        self.money = value

        return True
    
    def set_profit(self,value):

        self.profit = float(value)

        return True
    
    def set_loss(self,value):

        self.loss = float(value)

        return True
    
    def set_mode(self,value):
            
        self.mode = value

        return True
    
    def get_mode_env(self):

        return self.mode_env
    
    def get_mode_real(self):

        return self.mode_real