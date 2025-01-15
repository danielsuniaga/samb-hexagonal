from unittest import TestCase, mock

import unittest

import apis.controllers.GetEndPoint.GetEndPoint as ControllerGetEndPoint

class TestGetEndPoint(TestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetEndPoint.ControllerGetEndPoint()

    def test_GetEndPoint(self):

        result = self.controller.GetEndPoint()

        print("controller:",result)