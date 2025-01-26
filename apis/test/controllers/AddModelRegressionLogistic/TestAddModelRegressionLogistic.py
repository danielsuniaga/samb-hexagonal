from unittest import TestCase, mock

import unittest

import apis.controllers.AddModelRegressionLogistic.AddModelRegressionLogistic as ControllerAddModelRegressionLogistic

class TestAddModelRegressionLogistic(TestCase):
    
    controller = None

    def setUp(self):

        self.controller = ControllerAddModelRegressionLogistic.ControllerAddModelRegressionLogistic()

    def test_AddModelRegressionLogistic(self):

        result = self.controller.AddModelRegressionLogistic()

        print("controller:",result)