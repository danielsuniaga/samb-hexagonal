from unittest import TestCase, mock

import unittest

import apis.controllers.GetDataAnalysisDeriv.GetDataAnalysisDeriv as ControllerGetDataAnalysisDeriv

class TestGetDataAnalysisDeriv(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDeriv.ControllerGetDataAnalysisDeriv()

    async def GetDataAnalysisDeriv(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"
        
        result = await self.controller.GetDataAnalysisDeriv(request)

        print("controller:",result)

        return result