from decouple import config

class EntityPlatform: 

    deriv_platform = None

    def __init__(self):

        self.init_deriv_platform()

    def init_deriv_platform(self):

        self.deriv_platform = {
            'id':config("ID_DERIV_PLATFORM"),
            're':config("RE_DERIV_PLATFORM")
        }

        return True
    
    def get_re_deriv_platform(self):    
        
        return self.deriv_platform['re']
    
    def get_id_deriv_platform(self):
        
        return self.deriv_platform['id']    