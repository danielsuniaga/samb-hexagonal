from unittest import TestCase, mock

import unittest

import apis.controllers.GetDailyReportCrons.GetDailyReportCrons as ControllerGetDailyReportCrons

class TestGetDailyReportCrons(TestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDailyReportCrons.ControllerGetDailyReportCrons()

    def test_GetDailyReportCrons(self):

        result = self.controller.GetDailyReportCrons()

        print("controller:",result)