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