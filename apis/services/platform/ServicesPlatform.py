import apis.entities.platform.EntityPlatform as EntityPlatform

class ServicesPlatform():

    entity = None

    def __init__(self):

        self.entity = EntityPlatform.EntityPlatform()

    def get_id_platform_deriv(self):

        return self.entity.get_id_deriv_platform()
    
    def get_re_platform_deriv(self):

        return self.entity.get_re_deriv_platform()