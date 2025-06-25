from unittest import TestCase, mock

import unittest

import apis.controllers.SendDataSession.SendDataSession as ControllerSendDataSession

class TestSendDataSession(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerSendDataSession.ControllerSendDataSession()

    def test_send_data_controllers(self):

        return self.controller.send_data()

    def test_send_data(self):

        result = self.test_send_data_controllers()

        print("controller:", result)