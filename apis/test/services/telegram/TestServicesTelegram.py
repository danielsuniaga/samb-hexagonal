from unittest import TestCase, mock

import apis.services.telegram.ServicesTelegram as ServicesTelegram

class TestServicesTelegram(TestCase):

    ServicesTelegram = None

    def setUp(self):

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()

    def send_message(self):

        result = self.ServicesTelegram.send_message("mensaje","20241101205546")

        print(result)

        return True