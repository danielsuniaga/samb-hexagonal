import apis.entities.smtp.EntitySmtp as EntitySmtp

class ServicesSmtp():

    entity = None

    def __init__(self):

        self.entity = EntitySmtp.EntitySmtp()

    def generate_id(self):

        return self.entity.generate_id()
    
    def get_condition(self):

        return self.entity.get_condition()

    def init_data_add_notitificacion_exc(self,fecha,mensaje):

        return {
            'id':self.generate_id(),
            'mensaje':mensaje,
            'fecha':fecha,
            'condition':self.get_condition()
        }

    def send_notification_email(self,date,mensaje):

        return True