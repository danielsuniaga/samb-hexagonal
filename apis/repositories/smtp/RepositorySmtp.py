class RepositorySmtp():

    def add_notificacion_exc(self,mensaje):

        try:

            self.cursor_db.execute("INSERT INTO samb_notifications_exceptions_apis_independient(samb_notifications_exceptions_apis_independient.id,samb_notifications_exceptions_apis_independient.description, samb_notifications_exceptions_apis_independient.registration_date,samb_notifications_exceptions_apis_independient.update_date,samb_notifications_exceptions_apis_independient.condition, samb_notifications_exceptions_apis_independient.id_exceptions_api_id)VALUES(%s,%s,%s,%s,%s,%s)",[uuid.uuid4().hex, mensaje, self.fecha, self.fecha, "1", self.id_exceptions_api])

        except Exception:

            return False

        return True  