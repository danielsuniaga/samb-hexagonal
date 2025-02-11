from decouple import config

class EntityManagerDays():

    money = None

    profit = None

    loss = None

    mode = None

    mode_env = None

    def __init__(self):

        self.init_modes()

    def init_modes(self):

        self.mode = config("MODE")

        self.mode_env = config("MODE")

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