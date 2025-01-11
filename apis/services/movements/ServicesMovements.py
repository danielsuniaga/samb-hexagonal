import apis.repositories.movements.RepositoryMovements as RepositoryMovements
import apis.entities.movements.EntityMovements as EntityMovements   

class ServicesMovements():

    entity = None

    repository = None

    def __init__(self):

        self.repository = RepositoryMovements.RepositoryMovements()

        self.entity = EntityMovements.EntityMovements() 

    def set_candles(self,candles):
        
        return self.entity.set_candles(candles)
    
    def generate_id(self):

        return self.entity.generate_id()
    
    def get_condition(self):
        
        return self.entity.get_condition()

    def init_data_add_persistence(self,candles,data):

        return [
            (
                self.generate_id(),
                data['current_date'],
                data['current_date'],
                self.get_condition(),
                str(candle["open"]), 
                str(candle["close"]), 
                str(candle["high"]), 
                str(candle["low"]), 
                str(candle["epoch"]),
                data['data_entry']['id_entry']
            ) for candle in candles['candles']
        ]
    
    def add_movements_repository(self,data):

        return self.repository.add(data)
    
    def get_candles(self):

        return self.entity.get_candles()

    def add_persistence(self,data):

        data_persistence = self.init_data_add_persistence(self.get_candles(),data)

        return self.add_movements_repository(data_persistence)


    
