from deriv_api import DerivAPI

from decouple import config

import asyncio

import gc

import random

import logging

import uuid

logger_request    = logging.getLogger('ServicesBrokerRequest')
logger_response   = logging.getLogger('ServicesBrokerResponse')
logger_validation = logging.getLogger('ServicesAccountValidation')
logger_session    = logging.getLogger('ServicesBrokerSession')

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

    max_attempts_broker_deriv_execute_proposal = None

    _current_mode = None

    _broker_exec_id = None

    _account_id_broker = None

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

        self.init_max_attempts_broker_deriv_execute_proposal()

    def init_max_attempts_broker_deriv_execute_proposal(self):
        self.max_attempts_broker_deriv_execute_proposal = int(config("MAX_ATTEMPTS_BROKER_DERIV_EXECUTE_PROPOSAL"))
        return True
    
    def get_max_attempts_broker_deriv_execute_proposal(self):
        return self.max_attempts_broker_deriv_execute_proposal

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
        
        self.duration_seconds = (int(config("DURATION"))*60)+10

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

        self._current_mode = mode
        mode_str = "REAL" if mode is True else ("DEMO" if mode is False else "UNKNOWN")
        logger_validation.info(
            f"🔐 ACCOUNT TYPE CHECK | account_type: {mode_str} | "
            f"tokens_loaded: {self.tokens_asignado is not None}"
        )

        await self.init_token()

        token = await self.get_token_mode(mode)

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                response = await self.api.authorize(token)
                
                if response:
                    authorize_data = response.get('authorize', {})
                    self._account_id_broker = (
                        authorize_data.get('loginid')
                        or authorize_data.get('account_id', 'N/A')
                    )
                    logger_validation.info(
                        f"🔐 ACCOUNT TYPE CHECK | account_type: {mode_str} | "
                        f"account_id_broker: {self._account_id_broker} | "
                        f"currency: {authorize_data.get('currency', 'N/A')} | "
                        f"is_virtual: {authorize_data.get('is_virtual', 'N/A')}"
                    )
                    return {
                        'status': True,
                        'message': f'Conexion exitosa con deriv en intento {attempt}',
                        'attempts': attempt
                    }
                else:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': f'Respuesta vacía de autorización después de {max_attempts} intentos'}
                
            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(0, 1))
                    continue
                return {'status': False, 'message': f'Se genero una excepcion al chequear sincronizcion con deriv después de {max_attempts} intentos: {str(err)}'}
        
        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}

    async def init(self):

        await self.init_id_app()

        app_id = self.get_id_app()

        logger_session.info(
            f"🔌 BROKER SESSION | Event: CONNECTION_INIT | "
            f"app_id: {app_id} | tokens_loaded: {self.tokens_asignado is not None}"
        )

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                self.api = DerivAPI(app_id=app_id)
                
                # Verificar la conexión
                check_result = await self.check(False)
                
                if check_result['status']:
                    logger_session.info(
                        f"🔌 BROKER SESSION | Event: CONNECTION_OK | "
                        f"app_id: {app_id} | attempt: {attempt}"
                    )
                    return {
                        'status': True,
                        'message': f'Conexión inicializada correctamente en intento {attempt}',
                        'attempts': attempt
                    }
                else:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': f'Error al verificar conexión después de {max_attempts} intentos: {check_result["message"]}'}
            
            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(0, 1))
                    continue
                return {'status': False, 'message': f'Error al inicializar conexión después de {max_attempts} intentos: {err}'}

        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}
    
    async def closed(self):

        if not self.api:

            return {'status': False, 'message': 'No hay conexión activa con deriv para cerrar'}

        logger_session.info(
            f"🔌 BROKER SESSION | Event: CONNECTION_CLOSE_START"
        )

        max_attempts = self.get_max_attempts_broker_deriv()

        for attempt in range(1, max_attempts + 1):
            try:
                await self.api.disconnect()
                
                self.api = None

                gc.collect()

                logger_session.info(
                    f"🔌 BROKER SESSION | Event: CONNECTION_CLOSED_OK | attempt: {attempt}"
                )
                
                return {
                    'status': True,
                    'message': f'Conexión con Deriv cerrada correctamente en intento {attempt}',
                    'attempts': attempt
                }
            
            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(0, 1))
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
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': 'Deriv retornó respuesta inválida después de 5 intentos'}

                candles = candles_response.get("candles", [])

                # Validar que las velas no estén vacías
                if not candles:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': 'Deriv retornó velas vacías después de 5 intentos'}

                # Validar que las velas tengan la estructura correcta
                if not isinstance(candles, list) or len(candles) == 0:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': 'Estructura de velas inválida después de 5 intentos'}

                # Validar que cada vela tenga las propiedades básicas
                sample_candle = candles[0] if candles else {}
                required_fields = ['open', 'high', 'low', 'close']
                if not all(field in sample_candle for field in required_fields):
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
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
                    await asyncio.sleep(random.randint(0, 1))
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

        max_attempts = self.get_max_attempts_broker_deriv_execute_proposal()

        for attempt in range(1, max_attempts + 1):
            try:
                proposal_data = self.get_proposal_data(data['amount'],data['contract_type'],data['duration'],data['duration_unit'],data['symbol'])

                mode_str = "REAL" if self._current_mode is True else ("DEMO" if self._current_mode is False else "UNKNOWN")
                logger_request.info(
                    f"📤 BROKER REQUEST | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                    f"account_type: {mode_str} | "
                    f"contract_type: {data['contract_type']} | "
                    f"amount: {data['amount']} | "
                    f"symbol: {data['symbol']} | "
                    f"duration: {data['duration']}{data['duration_unit']} | "
                    f"attempt: {attempt}"
                )

                proposal_response = await self.api.proposal(proposal_data)

                if proposal_response is None:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
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
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': f'Error al generar la propuesta después de 5 intentos: {error_message}'}

            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(0, 1))
                    continue
                return {'status': False, 'message': f'Error al generar la propuesta después de 5 intentos: {err}'}

        return {'status': False, 'message': 'Falló después de 5 intentos'}

    
    async def execute_proposal(self, proposal_id):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        if proposal_id is None:

            return {'status': False, 'message': 'proposal_id es None'}

        max_attempts = self.get_max_attempts_broker_deriv_execute_proposal()

        for attempt in range(1, max_attempts + 1):
            try:
                execution_response = await self.api.buy({"buy": proposal_id, "price": 100})

                if execution_response is None:
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': f'La respuesta de la API es None después de {max_attempts} intentos'}

                if 'buy' in execution_response:
                    buy_data = execution_response.get('buy', {})
                    logger_response.info(
                        f"📥 BROKER RESPONSE OPEN | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"contract_id: {buy_data.get('contract_id', 'N/A')} | "
                        f"buy_price: {buy_data.get('buy_price', 'N/A')} | "
                        f"account_id_broker: {self._account_id_broker or 'N/A'} | "
                        f"attempt: {attempt}"
                    )
                    return {
                        'status': True,
                        'message': f'Posición ejecutada correctamente en intento {attempt}',
                        'execution_details': execution_response,
                        'attempts': attempt
                    }
                else:
                    error_message = execution_response.get("error", {}).get("message", "Respuesta desconocida")
                    if attempt < max_attempts:
                        await asyncio.sleep(random.randint(0, 1))
                        continue
                    return {'status': False, 'message': f'Error al ejecutar la posición después de {max_attempts} intentos: {error_message}'}

            except Exception as err:
                if attempt < max_attempts:
                    await asyncio.sleep(random.randint(0, 1))
                    continue
                return {'status': False, 'message': f'Error al ejecutar la posición después de {max_attempts} intentos: {err}'}

        return {'status': False, 'message': f'Falló después de {max_attempts} intentos'}
        
    async def generate_duration_contract(self):
    
        await asyncio.sleep(self.duration_seconds)

    async def check_position_result(self, contract_id):

        if self.api is None:
            logger_response.warning(
                f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                f"contract_id: {contract_id} | Result: FAILED | Reason: API not initialized"
            )
            return False

        max_api_errors        = self.get_max_attempts_broker_deriv()
        max_settlement_polls  = int(config("BROKER_CLOSE_MAX_POLLS", default=40))
        api_error_count       = 0
        settlement_poll_count = 0

        while True:
            try:
                response = await self.api.proposal_open_contract(
                    {"proposal_open_contract": 1, "contract_id": contract_id}
                )
                if not response or 'proposal_open_contract' not in response:
                    api_error_count += 1
                    if api_error_count >= max_api_errors:
                        logger_response.warning(
                            f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                            f"contract_id: {contract_id} | Result: FAILED | "
                            f"Reason: empty or missing proposal_open_contract | "
                            f"response_keys: {list(response.keys()) if isinstance(response, dict) else type(response).__name__}"
                        )
                        return False
                    await asyncio.sleep(random.randint(0, 1))
                    continue
                contract_info = response['proposal_open_contract']
                if not contract_info or not isinstance(contract_info, dict):
                    api_error_count += 1
                    if api_error_count >= max_api_errors:
                        logger_response.warning(
                            f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                            f"contract_id: {contract_id} | Result: FAILED | "
                            f"Reason: contract_info invalid | value: {contract_info}"
                        )
                        return False
                    await asyncio.sleep(random.randint(0, 1))
                    continue
                if not contract_info.get('is_sold'):
                    settlement_poll_count += 1
                    if settlement_poll_count >= max_settlement_polls:
                        logger_response.warning(
                            f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                            f"contract_id: {contract_id} | Result: FAILED | "
                            f"Reason: is_sold=False after {settlement_poll_count} settlement polls | "
                            f"status: {contract_info.get('status', 'N/A')} | "
                            f"expiry_time: {contract_info.get('expiry_time', 'N/A')}"
                        )
                        return False
                    logger_response.info(
                        f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"contract_id: {contract_id} | is_sold: False | "
                        f"settlement_poll: {settlement_poll_count}/{max_settlement_polls} | waiting 5s for broker settlement..."
                    )
                    await asyncio.sleep(5)
                    continue
                status = contract_info.get('status', 'unknown')
                profit_or_loss = contract_info.get('profit', 0)
                if status == 'won':
                    logger_response.info(
                        f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"contract_id: {contract_id} | "
                        f"profit: {profit_or_loss} | "
                        f"status: won | Win: True"
                    )
                    return self.get_won_contract(profit_or_loss, contract_info)
                elif status == 'lost':
                    logger_response.info(
                        f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"contract_id: {contract_id} | "
                        f"profit: {profit_or_loss} | "
                        f"status: lost | Win: False"
                    )
                    return self.get_lost_contract(profit_or_loss, contract_info)
                else:
                    api_error_count += 1
                    if api_error_count >= max_api_errors:
                        logger_response.warning(
                            f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                            f"contract_id: {contract_id} | Result: FAILED | "
                            f"Reason: unexpected status | status: {status} | "
                            f"profit: {profit_or_loss}"
                        )
                        return False
                    await asyncio.sleep(random.randint(0, 1))
                    continue
            except Exception as err:
                api_error_count += 1
                if api_error_count >= max_api_errors:
                    logger_response.warning(
                        f"📥 BROKER RESPONSE CLOSE | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"contract_id: {contract_id} | Result: FAILED | "
                        f"Reason: exception | error: {err}"
                    )
                    return False
                await asyncio.sleep(random.randint(0, 1))
                continue
        
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

    async def verify_contract_created(self, contract_id):

        try:
            response = await self.api.proposal_open_contract(
                {"proposal_open_contract": 1, "contract_id": contract_id}
            )
            if response and 'proposal_open_contract' in response:
                contract_info = response['proposal_open_contract']
                if contract_info and isinstance(contract_info, dict) and contract_info.get('contract_id'):
                    logger_response.info(
                        f"📋 BROKER CONTRACT VERIFIED | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"contract_id: {contract_id} | status: OK"
                    )
                    return True
            logger_response.warning(
                f"📋 BROKER CONTRACT VERIFIED | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                f"contract_id: {contract_id} | status: FAILED | "
                f"reason: contract not found in Deriv response"
            )
            return False
        except Exception as err:
            logger_response.warning(
                f"📋 BROKER CONTRACT VERIFIED | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                f"contract_id: {contract_id} | status: FAILED | "
                f"reason: exception | error: {err}"
            )
            return False

    async def add_entry(self, data):

        self._broker_exec_id = uuid.uuid4().hex[:12]

        max_retries = int(config("BROKER_ADD_ENTRY_MAX_RETRIES", default=1))
        contract_id = None

        for attempt in range(1, max_retries + 2):

            proposal_result = await self.generate_proposal(data)
            if not proposal_result['status']:
                if attempt <= max_retries:
                    logger_request.warning(
                        f"📤 BROKER REQUEST | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"Result: FAILED | Reason: proposal failed | "
                        f"attempt: {attempt}/{max_retries + 1} | Retrying..."
                    )
                    await asyncio.sleep(random.randint(1, 2))
                    continue
                return False

            execute_result = await self.execute_proposal(proposal_result['proposal_id'])
            if not execute_result['status']:
                if attempt <= max_retries:
                    logger_request.warning(
                        f"📤 BROKER REQUEST | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                        f"Result: FAILED | Reason: execute failed | "
                        f"attempt: {attempt}/{max_retries + 1} | Retrying..."
                    )
                    await asyncio.sleep(random.randint(1, 2))
                    continue
                return False

            contract_id = execute_result['execution_details'].get('buy', {}).get('contract_id')
            if not contract_id:
                logger_response.warning(
                    f"📥 BROKER RESPONSE OPEN | BrokerExec: {self._broker_exec_id or 'N/A'} | "
                    f"Result: FAILED | Reason: contract_id missing in buy response | "
                    f"buy_keys: {list(execute_result['execution_details'].get('buy', {}).keys())}"
                )
                return False

            verified = await self.verify_contract_created(contract_id)
            if not verified:
                return False

            break

        await self.generate_duration_contract()

        return await self.check_position_result(contract_id)
    
    def init_result_return_attent_initialization(self):

        return {'status': True, 'message': 'Success'}



