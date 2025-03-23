import apis.test.services.checktrendsexpansive.entity.EntityTestCheckTrendsExpansive as EntityTestCheckTrendsExpansive

class ServicesTestCheckTrendsExpansive():

    entity = None

    def __init__(self):

        self.entity = EntityTestCheckTrendsExpansive.EntityTestCheckTrendsExpansive()
    
    def get_data_entry_true(self):

        return self.entity.get_entrys_true()
    
    def get_data_indicators(self):

        return self.entity.get_indicators()
    
    def get_data_candles(self):

        return self.entity.get_candles()