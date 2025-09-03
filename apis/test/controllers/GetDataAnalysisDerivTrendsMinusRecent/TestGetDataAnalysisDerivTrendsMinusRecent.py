import unittest

import apis.controllers.GetDataAnalysisDerivTrendsMinusRecent.GetDataAnalysisDerivTrendsMinusRecent as ControllerGetDataAnalysisDerivTrendsMinusRecent

class TestGetDataAnalysisDerivTrendsMinusRecent(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsMinusRecent.ControllerGetDataAnalysisDerivTrendsMinusRecent()

    async def TestGetDataAnalysisDerivTrendsMinusRecent(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivMinusRecent(request)

        print("controller:",result)