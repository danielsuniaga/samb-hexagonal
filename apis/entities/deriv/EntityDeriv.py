from deriv_api import DerivAPI

from decouple import config

import asyncio

import gc

import random

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

    conection_broker_atents = None

    tokens = None

    tokens_asignado = None

    max_attempts_broker_deriv = None

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

        self.init_conection_broker_atents()

        self.init_tokens()

        self.init_max_attempts_broker_deriv()

    def init_max_attempts_broker_deriv(self):
        self.max_attempts_broker_deriv = int(config("MAX_ATTEMPTS_BROKER_DERIV"))
        return True
    
    def get_max_attempts_broker_deriv(self):
        return self.max_attempts_broker_deriv

    def init_tokens(self):

        self.tokens = {
            'orion': {
                'real': config("TOKEN_DERIV_REAL_ORION"),
                'demo': config("TOKEN_DERIV_DEMO_ORION"),
            },
            'ursa_major': {
                'real': config("TOKEN_DERIV_REAL_URSA_MAJOR"),
                'demo': config("TOKEN_DERIV_DEMO_URSA_MAJOR"),
            },
            'ursa_minor': {
                'real': config("TOKEN_DERIV_REAL_URSA_MINOR"),
                'demo': config("TOKEN_DERIV_DEMO_URSA_MINOR"),
            },
            'cassiopeia': {
                'real': config("TOKEN_DERIV_REAL_CASSIOPEIA"),
                'demo': config("TOKEN_DERIV_DEMO_CASSIOPEIA"),
            },
            'scorpius': {
                'real': config("TOKEN_DERIV_REAL_SCORPIUS"),
                'demo': config("TOKEN_DERIV_DEMO_SCORPIUS"),
            },
        }
        return True
    
    def get_tokens(self,account_type):

        if account_type in self.tokens:

            return self.tokens[account_type]

        return None
    
    def get_tokens_orion(self):

        return self.get_tokens('orion')
    
    def get_tokens_ursa_major(self):

        return self.get_tokens('ursa_major')
    
    def get_tokens_ursa_minor(self):
        
        return self.get_tokens('ursa_minor')
    
    def get_tokens_cassiopeia(self):
                        
        return self.get_tokens('cassiopeia')
    
    def get_tokens_scorpius(self):
            
        return self.get_tokens('scorpius')
    
    def init_tokens_asignado(self,account_type):

        self.tokens_asignado = account_type

        return True
    
    def get_tokens_asignado(self):

        return self.tokens_asignado

    def init_conection_broker_atents(self):

        self.conection_broker_atents = {
            'atents': config("BROKER_CONECTION_ATENTS"),
            'duration_latency': config("LATENCY_CONECTION_DURATION")
        }

        return True
    
    def get_conection_broker_atents(self):

        return self.conection_broker_atents    

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
    
    def get_duration_seconds(self):

        return self.duration_seconds

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

        self.tokens = self.get_tokens_asignado()

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

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                response = await self.api.authorize(token)
                
                if response:
                    return {
                        'status': True,
                        'message': f'Conexion exitosa con deriv en intento {attempt}',
                        'attempts': attempt
                    }
                else:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': f'Respuesta vacía de autorización después de {max_attempts} intentos'}
                
            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(1, 3))
                    continue
                return {'status': False, 'message': f'Se genero una excepcion al chequear sincronizcion con deriv después de {max_attempts} intentos: {str(err)}'}
        
        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}

    async def init(self):

        await self.init_id_app()

        app_id = self.get_id_app()

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                self.api = DerivAPI(app_id=app_id)
                
                # Verificar la conexión
                check_result = await self.check(False)
                
                if check_result['status']:
                    return {
                        'status': True,
                        'message': f'Conexión inicializada correctamente en intento {attempt}',
                        'attempts': attempt
                    }
                else:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': f'Error al verificar conexión después de {max_attempts} intentos: {check_result["message"]}'}
            
            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(1, 3))
                    continue
                return {'status': False, 'message': f'Error al inicializar conexión después de {max_attempts} intentos: {err}'}

        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}
    
    async def closed(self):

        if not self.api:

            return {'status': False, 'message': 'No hay conexión activa con deriv para cerrar'}
        
        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                await self.api.disconnect()
                
                self.api = None

                gc.collect()
                
                return {
                    'status': True,
                    'message': f'Conexión con Deriv cerrada correctamente en intento {attempt}',
                    'attempts': attempt
                }
            
            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(1, 3))
                    continue
                return {'status': False, 'message': f'Se generó una excepción al cerrar la conexión con Deriv después de {max_attempts} intentos: {err}'}
        
        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}
    
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

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                data = await self.init_data_ticks_history()
                candles_response = await self.api.ticks_history(data)

                # Validar que la respuesta tenga la estructura esperada
                if not candles_response or not isinstance(candles_response, dict):
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': 'Deriv retornó respuesta inválida después de 5 intentos'}

                candles = candles_response.get("candles", [])

                # Validar que las velas no estén vacías
                if not candles:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': 'Deriv retornó velas vacías después de 5 intentos'}

                # Validar que las velas tengan la estructura correcta
                if not isinstance(candles, list) or len(candles) == 0:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': 'Estructura de velas inválida después de 5 intentos'}

                # Validar que cada vela tenga las propiedades básicas
                sample_candle = candles[0] if candles else {}
                required_fields = ['open', 'high', 'low', 'close']
                if not all(field in sample_candle for field in required_fields):
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': 'Velas con campos faltantes después de 5 intentos'}

                # Éxito - respuesta válida
                return {
                    'status': True,
                    'message': f'{len(candles)} velas obtenidas correctamente en intento {attempt}',
                    'candles': candles,
                    'attempts': attempt
                }

            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(1, 3))
                    continue
                return {'status': False, 'message': f'Error después de {max_attempts} intentos: {err}'}

        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}
        
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

        if data['amount'] <= 0:
            return {'status': False, 'message': 'El monto debe ser mayor que 0'}

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                proposal_data = self.get_proposal_data(data['amount'],data['contract_type'],data['duration'],data['duration_unit'],data['symbol'])

                proposal_response = await self.api.proposal(proposal_data)

                if proposal_response is None:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': 'La respuesta de la API es None después de 5 intentos'}

                if 'proposal' in proposal_response:
                    # ✅ ÉXITO - Retorna inmediatamente sin más intentos
                    return {
                        'status': True,
                        'message': f'Propuesta generada correctamente en intento {attempt}',
                        'proposal_id': proposal_response["proposal"]["id"],
                        'proposal_details': proposal_response,
                        'attempts': attempt
                    }
                else:
                    error_message = proposal_response.get("error", {}).get("message", "Respuesta desconocida")
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': f'Error al generar la propuesta después de 5 intentos: {error_message}'}

            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(1, 3))
                    continue
                return {'status': False, 'message': f'Error al generar la propuesta después de 5 intentos: {err}'}

        return {'status': False, 'message': 'Falló después de 5 intentos'}

    
    async def execute_proposal(self, proposal_id):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        if proposal_id is None:

            return {'status': False, 'message': 'proposal_id es None'}

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                execution_response = await self.api.buy({"buy": proposal_id, "price": 100})

                if execution_response is None:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': f'La respuesta de la API es None después de {max_attempts} intentos'}

                if 'buy' in execution_response:
                    return {
                        'status': True,
                        'message': f'Posición ejecutada correctamente en intento {attempt}',
                        'execution_details': execution_response,
                        'attempts': attempt
                    }
                else:
                    error_message = execution_response.get("error", {}).get("message", "Respuesta desconocida")
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(1, 3))
                        continue
                    return {'status': False, 'message': f'Error al ejecutar la posición después de {max_attempts} intentos: {error_message}'}

            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(1, 3))
                    continue
                return {'status': False, 'message': f'Error al ejecutar la posición después de {max_attempts} intentos: {err}'}

        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}
        
    async def generate_duration_contract(self):
    
        await asyncio.sleep(self.duration_seconds)

    async def check_position_result(self, contract_id):

        if self.api is None:
            
            return {'status': False, 'message': 'API no inicializada'}

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(max_attempts):
            
            try:

                response = await self.api.proposal_open_contract(
                    {"proposal_open_contract": 1, "contract_id": contract_id}
                )
                
                if not response or 'proposal_open_contract' not in response:
                    
                    if attempt == max_attempts - 1:
                        return {'status': False, 'message': f'La respuesta no contiene información válida sobre el contrato después de {max_attempts} intentos'}
                    
                    await asyncio.sleep(random.randint(1, 3))
                    continue

                contract_info = response['proposal_open_contract']
                
                # Verificar que tengamos contract_details completos
                if not contract_info or not isinstance(contract_info, dict):
                    
                    if attempt == max_attempts - 1:
                        return {'status': False, 'message': f'contract_info no válido después de {max_attempts} intentos'}
                    
                    await asyncio.sleep(random.randint(1, 3))
                    continue

                if not contract_info.get('is_sold'):
                    
                    if attempt == max_attempts - 1:
                        return {'status': False, 'message': f'El contrato aún no ha sido vendido después de {max_attempts} intentos'}
                    
                    await asyncio.sleep(random.randint(1, 3))
                    continue

                status = contract_info.get('status', 'unknown')
                profit_or_loss = contract_info.get('profit', 0)

                if status == 'won':
                    
                    return self.get_won_contract(profit_or_loss, contract_info)
                
                elif status == 'lost':

                    return self.get_lost_contract(profit_or_loss, contract_info)
                
                else:
                    
                    if attempt == max_attempts - 1:
                        return {'status': False, 'message': f'Estado desconocido: {status} después de {max_attempts} intentos'}
                    
                    await asyncio.sleep(random.randint(1, 3))
                    continue

            except Exception as err:
                
                if attempt == max_attempts - 1:
                    return {'status': False, 'message': f'Error al consultar contrato después de {max_attempts} intentos: {err}'}
                
                await asyncio.sleep(random.randint(1, 3))
                continue

        return {'status': False, 'message': f'No se pudo obtener resultado después de {max_attempts} intentos'}
        
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
            return {
                'status': False,
                'message': f'Error al generar propuesta: {result.get("message", "Error desconocido")}',
                'error_stage': 'generate_proposal',
                'contract_details': {}
            }

        result = await self.execute_proposal(result['proposal_id'])

        if not result['status']:
            return {
                'status': False,
                'message': f'Error al ejecutar propuesta: {result.get("message", "Error desconocido")}',
                'error_stage': 'execute_proposal',
                'contract_details': {}
            }

        await self.generate_duration_contract()

        return await self.check_position_result(result['execution_details']['buy']['contract_id'])
    
    def init_result_return_attent_initialization(self):

        return {'status': True, 'message': 'Success'}



