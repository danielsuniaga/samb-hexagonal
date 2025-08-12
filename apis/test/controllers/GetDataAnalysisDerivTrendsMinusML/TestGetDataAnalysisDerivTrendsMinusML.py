from unittest import TestCase, mock

import unittest

import apis.controllers.GetDataAnalysisDerivTrendsMinusML.GetDataAnalysisDerivTrendsMinusML as ControllerGetDataAnalysisDerivTrendsMinusML

class TestGetDataAnalysisDerivTrendsMinusML(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):
        self.controller = ControllerGetDataAnalysisDerivTrendsMinusML.ControllerGetDataAnalysisDerivTrendsMinusML()

    async def TestGetDataAnalysisDerivMinusML(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivMinusML(request)

        print("controller:",result)

        return result