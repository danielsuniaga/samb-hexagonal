from unittest import TestCase, mock

import unittest

import apis.controllers.AddModels.AddModels as ControllerAddModels

class TestAddModels(TestCase):
    
    controller = None

    def setUp(self):

        self.controller = ControllerAddModels.ControllerAddModels()

    def test_AddModels(self):

        result = self.controller.AddModels()

        print("controller:",result)