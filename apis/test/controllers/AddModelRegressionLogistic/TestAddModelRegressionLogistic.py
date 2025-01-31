from unittest import TestCase, mock

import unittest

import apis.controllers.AddModels.AddModels as ControllerAddModels

class TestAddModelRegressionLogistic(TestCase):
    
    controller = None

    def setUp(self):

        self.controller = ControllerAddModels.ControllerAddModels()

    def test_AddModelRegressionLogistic(self):

        result = self.controller.AddModels()

        print("controller:",result)