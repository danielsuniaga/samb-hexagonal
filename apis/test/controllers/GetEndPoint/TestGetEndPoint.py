from unittest import TestCase, mock

import unittest

import apis.controllers.GetEndPoint.GetEndPoint as ControllerGetEndPoint

class TestGetEndPoint(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetEndPoint.ControllerGetEndPoint()

    async def test_GetEndPoint(self):

        result = await  self.controller.GetEndPoint()

        print("controller:",result)

    def test_send_email(self):

        result = self.controller.send_email()

        print("controller:",result)