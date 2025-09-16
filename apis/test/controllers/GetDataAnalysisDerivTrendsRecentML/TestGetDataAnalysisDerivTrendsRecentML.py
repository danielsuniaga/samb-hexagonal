import unittest

import apis.controllers.GetDataAnalysisDerivTrendsRecentML.GetDataAnalysisDerivTrendsRecentML as ControllerGetDataAnalysisDerivTrendsRecentML

class TestGetDataAnalysisDerivTrendsRecentML(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsRecentML.ControllerGetDataAnalysisDerivTrendsRecentML()

    async def TestGetDataAnalysisDerivTrendsRecentML(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivTrendsRecentML(request)

        print("controller:",result)