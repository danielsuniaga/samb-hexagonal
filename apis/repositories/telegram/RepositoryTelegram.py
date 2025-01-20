from django.db import connection

class RepositoryTelegram():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_send_message_api_telegram(samb_send_message_api_telegram.id,samb_send_message_api_telegram.type,samb_send_message_api_telegram.message,samb_send_message_api_telegram.chat,samb_send_message_api_telegram.response_method,samb_send_message_api_telegram.registration_date,samb_send_message_api_telegram.update_date,samb_send_message_api_telegram.condition)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",[data['id'],data['type'],data['message'],data['chat'],data['response_method'],data['current_date'],data['current_date'],data['condition']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys_results '+str(err)}
        
        return {'status':True,'msj':'Success'}

        return True