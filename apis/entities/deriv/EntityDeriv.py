from deriv_api import DerivAPI

from decouple import config

import asyncio

class EntityDeriv():

    id_app = None

    api = None

    par = None

    count = None

    end = None

    style = None

    granularity = None

    duration = None

    duration_unit = None

    duration_seconds = None

    def __init__(self):

        self.init_par()

        self.init_count()

        self.init_end()

        self.init_style()

        self.init_granularity()

        self.init_duration()

        self.init_duration_unit()

        self.init_proposal_env()

        self.init_duration_seconds()

    def add_result_positions(self,data,result,index):

        data[index] = result

        return data

    def init_proposal_env(self):

        self.proposal_env = {
            'basis':config("PROPOSAL_BASIS"),
            'currency':config("PROPOSAL_CURRENCY")
        }

        return True
    
    def get_proposal_env_basis(self):

        return self.proposal_env['basis']
    
    def get_proposal_env_currency(self):

        return self.proposal_env['currency']

    def init_duration_unit(self):     

        self.duration_unit = config("DURATION_UNIT")

        return True
    
    def init_duration_seconds(self):
        
        self.duration_seconds = (int(config("DURATION"))*60)+5

        return True
    
    def get_duration_unit(self):     

        return self.duration_unit

    def init_duration(self):

        self.duration = int(config("DURATION"))

        return True
    
    def get_duration(self):

        return self.duration

    def init_granularity(self):

        self.granularity = int(config("GRANULARITY"))

        return True
    
    def get_granularity(self):

        return self.granularity

    def init_style(self):

        self.style = config("STYLE")

        return True
    
    def get_style(self):

        return self.style

    def init_end(self):

        self.end = config("END")

        return True
    
    def get_end(self):

        return self.end

    def init_count(self):

        self.count = int(config("COUNT"))

        return True
    
    def get_count(self):

        return self.count

    def init_par(self):

        self.par = config("PAR")

        return True
    
    def get_par(self):

        return self.par

    async def init_id_app(self):

        self.id_app = int(config("ID_APP"))

        return True

    def get_id_app(self):

        return self.id_app
    
    async def init_token(self):

        self.tokens = {
            'demo': config("TOKEN_DERIV_DEMO"),
            'real': config("TOKEN_DERIV_REAL")
        }

        return True
    
    def get_token_real(self):

        return self.tokens['real']
    
    def get_token_demo(self):

        return self.tokens['demo']
    
    async def get_token_mode(self,mode):

        if not mode:

            return self.get_token_demo()
        
        return self.get_token_real()
    
    async def check(self,mode):

        await self.init_token()

        token = await self.get_token_mode(mode)

        try:

            response = await self.api.authorize(token)
            
        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al chequear sincronizcion con deriv: '+str(err)}
        
        return {'status': True, 'message':'Conexion exitosa con deriv'}

    async def init(self):

        await self.init_id_app()

        app_id = self.get_id_app()

        try:

            self.api = DerivAPI(app_id=app_id)
        
        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al inicializar la conexion con deriv: '+str(err)}
        
        return await self.check(False)
    
    async def closed(self):

        if not self.api:

            return {'status': False, 'message': 'No hay conexión activa con deriv para cerrar'}
        
        try:

            await self.api.disconnect()
        
        except Exception as err:

            return {'status': False, 'message': f'Se generó una excepción al cerrar la conexión con Deriv: {err}'}
        
        return {'status': True, 'message': 'Conexión con Deriv cerrada correctamente'}
    
    async def init_data_ticks_history(self):

        return {
                "ticks_history": self.get_par(),  
                "count": self.get_count(),           
                "end": self.get_end(),          
                "style": self.get_style(),       
                "granularity": self.get_granularity() 
            }
    
    async def get_candles(self):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        try:

            data = await self.init_data_ticks_history()

            candles_response = await self.api.ticks_history(data)

            candles = candles_response.get("candles", [])

            return {
                'status': True,
                'message': f'{len(candles)} velas obtenidas correctamente',
                'candles': candles
            }

        except Exception as err:

            return {'status': False, 'message': f'Error al obtener velas: {err}'}
        
    def get_proposal_data(self,amount,contract_type,duration,duration_unit,symbol):

        return {
                "proposal": 1,
                "amount": amount,
                "basis": self.get_proposal_env_basis(),
                "contract_type": contract_type,
                "currency": self.get_proposal_env_currency(),
                "duration": duration,
                "duration_unit": duration_unit,
                "symbol": symbol
            }
        
    async def generate_proposal(self,data):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        try:

            if data['amount'] <= 0:

                return {'status': False, 'message': 'El monto debe ser mayor que 0'}

            proposal_data = self.get_proposal_data(data['amount'],data['contract_type'],data['duration'],data['duration_unit'],data['symbol'])

            proposal_response = await self.api.proposal(proposal_data)

            if proposal_response is None:

                return {'status': False, 'message': 'La respuesta de la API es None'}

            if 'proposal' in proposal_response:

                return {
                    'status': True,
                    'message': 'Propuesta generada correctamente',
                    'proposal_id': proposal_response["proposal"]["id"],
                    'proposal_details': proposal_response,
                }
            
            else:

                error_message = proposal_response.get("error", {}).get("message", "Respuesta desconocida")

                return {'status': False, 'message': f'Error al generar la propuesta: {error_message}'}

        except Exception as err:

            return {'status': False, 'message': f'Error al generar la propuesta: {err}'}

        return True
    
    async def execute_proposal(self, proposal_id):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        if proposal_id is None:

            return {'status': False, 'message': 'proposal_id es None'}

        try:

            execution_response = await self.api.buy({"buy": proposal_id, "price": 100})

            if execution_response is None:

                return {'status': False, 'message': 'La respuesta de la API es None'}

            if 'buy' in execution_response:

                return {
                    'status': True,
                    'message': 'Posición ejecutada correctamente',
                    'execution_details': execution_response,
                }
            
            else:

                error_message = execution_response.get("error", {}).get("message", "Respuesta desconocida")

                return {'status': False, 'message': f'Error al ejecutar la posición: {error_message}'}

        except Exception as err:
            
            return {'status': False, 'message': f'Error al ejecutar la posición: {err}'}
        
    async def generate_duration_contract(self):
    
        await asyncio.sleep(self.duration_seconds)

    async def check_position_result(self, contract_id):

        if self.api is None:
            
            return {'status': False, 'message': 'API no inicializada'}

        try:

            response = await self.api.proposal_open_contract(
                {"proposal_open_contract": 1, "contract_id": contract_id}
            )
            if not response or 'proposal_open_contract' not in response:

                return {'status': False, 'message': 'La respuesta no contiene información válida sobre el contrato'}

            contract_info = response['proposal_open_contract']

            if not contract_info.get('is_sold'):

                return {'status': False, 'message': 'El contrato aún no ha sido vendido o completado'}

            status = contract_info.get('status', 'unknown')

            profit_or_loss = contract_info.get('profit', 0)

            if status == 'won':
                
                return self.get_won_contract(profit_or_loss, contract_info)
            
            elif status == 'lost':

                return self.get_lost_contract(profit_or_loss, contract_info)
            
            else:

                return {'status': False, 'message': f'Estado desconocido: {status}'}

        except Exception as err:

            return {'status': False, 'message': f'Error al consultar contrato: {err}'}
        
    def get_won_contract(self, profit, contract_info):

        return {
            'status': True,
            'message': 'La posición fue exitosa',
            'profit': profit,
            'contract_details': contract_info,
        }

    def get_lost_contract(self, loss, contract_info):

        return {
            'status': False,
            'message': 'La posición fue perdedora',
            'loss': loss,
            'contract_details': contract_info,
        }
        
    async def add_entry(self, data):

        result = await self.generate_proposal(data)

        if not result['status']:
            return False

        result = await self.execute_proposal(result['proposal_id'])

        if not result['status']:
            return False

        await self.generate_duration_contract()

        return await self.check_position_result(result['execution_details']['buy']['contract_id'])
    


