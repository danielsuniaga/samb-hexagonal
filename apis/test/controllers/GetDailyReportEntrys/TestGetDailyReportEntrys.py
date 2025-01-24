from unittest import TestCase, mock

import unittest

import apis.controllers.GetDailyReportEntrys.GetDailyReportEntrys as ControllerGetDailyReportEntrys

class TestGetDailyReportEntrys(TestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDailyReportEntrys.ControllerGetDailyReportEntrys()

    def test_GetDailyReportEntrys(self):

        result = self.controller.GetDailyReportEntrys()

        print("controller:",result)