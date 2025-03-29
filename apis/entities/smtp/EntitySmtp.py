import uuid

from decouple import config

from email import message

import smtplib

import email.message

import traceback

class EntitySmtp():

    cuerpo = None

    condition = None

    id_exceptions_api = None

    subject = None

    message = ""

    from_email = None

    email=None

    destinatario = None

    server = None

    subject_reports = None

    apis_name = None

    def __init__(self):

        self.init_condition()

        self.init_id_exceptions_api()

        self.init_server()

        self.init_port()

        self.init_subject()

        self.init_email()

        self.init_password_email()

        self.init_destinatario()

        self.set_message_body()

        self.init_from_email()

        self.init_subject_reports()

    def set_apis_name(self, apis):

        self.apis_name = apis

        return True
    
    def get_apis_name(self):

        if self.apis_name is not None:

            return self.apis_name

        return None

    def init_subject_reports(self):

        self.subject_reports = {
            "daily":"Daily report ("+config("PROJECT_NAME")+") | SAMB | TRADING",
        }

        return True
    
    def get_reports_subject_daily(self):

        return self.subject_reports["daily"]

    def init_server(self):

        self.server = config("SERVER_SMTP")

    def init_port(self):

        self.port = config("PORT_SMTP")

    def init_password_email(self):

        self.password_email = config("SECRET_EMAIL")

        return True

    def init_destinatario(self):

        self.destinatario = config("EMAIL_RECIPIENT")

        return True

    def init_email(self):

        self.email=config("EMAIL_SEND")

    def init_from_email(self):

        self.from_email = "Notificaciones  SAMB <"+self.email+">"

        return True

    def init_subject(self):

        self.subject = "Notificaciones de excepciones - ("+config("PROJECT_NAME")+") - "+str(self.apis_name)+" | SAMB | TRADING "

        return True
    
    def set_subject(self,subject):

        self.subject = subject

        return True
    
    def set_message_body(self):

        self.cuerpo = """ <tr> <td bgcolor="#ffffff" style="padding: 20px 30px 5px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #340049; font-family: Arial, sans-serif; font-size: 24px;"><b>Details</b></td> </tr> <tr> <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;text-align: justify;">"""+self.message+"""</td> </tr> <tr> <td> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td width="260" valign="top"> </td> <td style="font-size: 4; line-height: 0;" width="20"> &nbsp; </td> <td width="260" valign="top"> </td> </tr> </table> </td> </tr> </table> </td> </tr>  """
        
        return True

    def set_message(self,mensaje):

        self.message = mensaje

        return True

    def init_id_exceptions_api(self):

        self.id_exceptions_api = config("ID_EXCEPTIONS_API")

    def get_id_exceptions_apis(self):

        return self.id_exceptions_api

    def init_condition(self):

        self.condition = config("CONDITION")

    def get_condition(self):

        return self.condition

    def generate_id(self):

        return uuid.uuid4().hex
    
    def init_destinatario(self):

        self.destinatario = config("EMAIL_RECIPIENT")

        return True
    
    def get_encabezado(self): 

        return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />	<title>".$msj_titulo."</title> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> </head> <body style="margin: 0; padding: 0;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="padding: 10px 0 30px 0;"> <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px solid #cccccc; border-collapse: collapse;">	<tr> <td align="center" bgcolor="#ffffff" style="padding: 5px 5px 5px 5px;"> """
    
    def get_pie(self):

        return """</td> </tr> <tr> <td bgcolor="#340049" style="padding: 30px 30px 30px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #ffffff; font-family: Arial, sans-serif; font-size: 14px;" width="100%"><font color="#ffffff"></font><i>Esta es una cuenta de correo solo informativa, por favor no responder este correo.</i></td> </tr> </table>	</td> </tr>	</table> </td> </tr> </table> </body> </html>"""
    
    def get_cuerpo(self):

        return self.cuerpo
    
    def init_body(self):
        
        return self.get_encabezado()+self.get_cuerpo()+self.get_pie()
    
    def send_email(self, mensaje):

        self.init_subject()

        self.set_message(mensaje)

        self.set_message_body()

        body = self.init_body()

        try:
            _msg = email.message.Message()
            _msg["Subject"] = self.subject
            _msg["From"] = self.from_email
            _msg["To"] = self.destinatario
            _password = self.password_email
            _correo = self.email
            _msg.add_header("Content-Type", "text/html")
            _msg.set_payload(body)

            _s = smtplib.SMTP(self.server, self.port)
            _s.starttls()
            _s.login(_correo, _password)
            _s.sendmail(_msg["From"], [_msg["To"]], _msg.as_string())
            _s.quit()

        except Exception as err:
            return {"status": False, "message": "Hubo una incidencia en el envío del mensaje SMTP: " + str(err)}

        return True