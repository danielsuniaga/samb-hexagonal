import asyncio
import apis.entities.deriv.EntityDeriv as EntityDeriv

class ServicesDeriv():

    entity = None

    def __init__(self):

        self.entity = EntityDeriv.EntityDeriv()

    def init_tokens_asignado(self,account):

        return self.entity.init_tokens_asignado(account)

    def get_tokens_orion(self):

        return self.entity.get_tokens_orion()
    
    def get_tokens_ursa_major(self):

        return self.entity.get_tokens_ursa_major()
    
    def get_tokens_ursa_minor(self):
            
        return self.entity.get_tokens_ursa_minor()
    
    def get_tokens_casiopeia(self):
   
        return self.entity.get_tokens_casiopeia()
    
    def get_tokens_scorpius(self):
            
        return self.entity.get_tokens_scorpius()

    def get_conection_broker_atents(self):

        return self.entity.get_conection_broker_atents()
    
    async def init(self):

        conection_broker = self.get_conection_broker_atents()

        max_attempts = self.get_max_attempts(conection_broker)

        sleep_duration = self.get_sleep_duration(conection_broker)

        return await self.attempt_initialization(max_attempts, sleep_duration)

    def get_max_attempts(self, conection_broker):

        return int(conection_broker.get('max_attempts', 3))

    def get_sleep_duration(self, conection_broker):

        return int(conection_broker.get('duration_latency', 500)) / 1000 
    
    def init_result_return_attent_initialization(self):

        return self.entity.init_result_return_attent_initialization()

    async def attempt_initialization(self, max_attempts, sleep_duration):

        attempt = 0

        result_return = self.init_result_return_attent_initialization()

        while attempt < max_attempts:

            result = await self.entity.init()

            if result.get('status', False):

                return result

            attempt += 1

            result_return = result

            await asyncio.sleep(sleep_duration)

        return {'status': False, 'message': 'Max attempts reached, initialization failed'+' - '+str(result_return['message'])}
    
    async def closed(self):

        return await self.entity.closed()
    
    async def check(self,mode):

        return await self.entity.check(mode)
    
    def get_par(self):

        return self.entity.get_par()
    
    async def get_candles(self):

        return await self.entity.get_candles()
    
    def get_duration(self):
        
        return self.entity.get_duration()
    
    def get_duration_unit(self):    

        return self.entity.get_duration_unit()
    
    async def add_entry(self,data):

        return await self.entity.add_entry(data)
    
    def add_result_positions_mode(self,data,mode):

        return self.entity.add_result_positions(data,mode,'mode')
    
    def add_result_positions_candle_analisys(self,data,candle):

        return self.entity.add_result_positions(data,candle,'candle_analisys')
    
    def add_result_positions_condition_entry(self,data,condition):
        
        return self.entity.add_result_positions(data,condition,'condition_entry')
    
    def add_result_positions_amount(self,data,amount):

        return self.entity.add_result_positions(data,amount,'amount')
    
    def add_result_positions_current_date(self,data,date):

        return self.entity.add_result_positions(data,date,'current_date')
    
    def add_result_positions_id_cronjobs(self,data,id_cronjobs):

        return self.entity.add_result_positions(data,id_cronjobs,'id_cronjobs')
    
    def add_result_positions_id_methodology(self,data,id_methodology):

        return self.entity.add_result_positions(data,id_methodology,'id_methodology') 
    
    def add_result_positions_re_platform(self,data,re_platform):    

        return self.entity.add_result_positions(data,re_platform,'re_entry_platform')
    
    def add_result_positions_data_entrys(self,result,data):

        return self.entity.add_result_positions(result,data,'data_entry')
    
    def get_duration_seconds(self):

        return self.entity.get_duration_seconds()  