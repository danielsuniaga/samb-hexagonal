from deriv_api import DerivAPI

from decouple import config

class EntityDeriv():

    id_app = None

    api = None

    par = None

    count = None

    end = None

    style = None

    granularity = None

    def __init__(self):

        self.init_par()

        self.init_count()

        self.init_end()

        self.init_style()

        self.init_granularity()

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
        
        return {'status': True, 'msj':'Conexion exitosa con deriv'}

    async def init(self):

        await self.init_id_app()

        app_id = self.get_id_app()

        try:

            self.api = DerivAPI(app_id=app_id)
        
        except Exception as err:

            return {'status': False, 'msj':'Se genero una excepcion al inicializar la conexion con deriv: '+str(err)}
        
        return await self.check(False)
    
    async def closed(self):

        if not self.api:

            return {'status': False, 'msj': 'No hay conexión activa con deriv para cerrar'}
        
        try:

            await self.api.disconnect()
        
        except Exception as err:

            return {'status': False, 'msj': f'Se generó una excepción al cerrar la conexión con Deriv: {err}'}
        
        return {'status': True, 'msj': 'Conexión con Deriv cerrada correctamente'}
    
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

            return {'status': False, 'msj': 'API no inicializada'}

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

            return {'status': False, 'msj': f'Error al obtener velas: {err}'}

