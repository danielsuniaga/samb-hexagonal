import apis.entities.smtp.EntitySmtp as EntitySmtp

import apis.repositories.smtp.RepositorySmtp as RepositorySmtp

class ServicesSmtp():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntitySmtp.EntitySmtp()

        self.repository = RepositorySmtp.RepositorySmtp()

    def generate_id(self):

        return self.entity.generate_id()
    
    def get_condition(self):

        return self.entity.get_condition()
    
    def get_id_exceptions_apis(self):

        return self.entity.get_id_exceptions_apis()

    def init_data_add_notitificacion_exc(self,fecha,mensaje):

        return {
            'id':self.generate_id(),
            'mensaje':mensaje,
            'fecha':fecha,
            'condition':self.get_condition(),
            'id_exceptions_apis':self.get_id_exceptions_apis()
        }
    
    def add_notificacion_exc(self,data):

        return self.repository.add_notificacion_exc(data)

    def send_email(self,mensaje):

        return self.entity.send_email(mensaje)

    def send_notification_email(self,date,mensaje):

        data = self.init_data_add_notitificacion_exc(date,mensaje)

        result = self.add_notificacion_exc(data)

        result_send = self.send_email(mensaje)

        return True