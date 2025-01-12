import apis.test.services.deriv.entity.EntityTestServicesDeriv as EntityTestServicesDeriv

class ServicesTestServicesDeriv():

    entity = None

    def __init__(self):

        self.entity = EntityTestServicesDeriv.EntityTestServicesDeriv()

    def get_data_entry_true(self):

        return self.entity.get_entrys_true()
    
    def get_data_entry_false(self):

        return self.entity.get_entrys_false()
    
    def get_data_candles(self):

        return self.entity.get_candles()
    
    def get_data_indicators(self):

        return self.entity.get_indicators()    
    
