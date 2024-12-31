from unittest import TestCase, mock

import apis.services.smtp.ServicesSmtp as ServicesSmtp

class TestServicesSmtp(TestCase):

    service = None

    def setUp(self):

        self.service = ServicesSmtp.ServicesSmtp()

    def test_send_notitication_email(self):

        result = self.service.send_notification_email('20241230162400','test')

        return result