import unittest

import apis.controllers.GetDataAnalysisDerivTrendsExpansiveRecentML.GetDataAnalysisDerivTrendsExpansiveRecentML as ControllerGetDataAnalysisDerivTrendsExpansiveRecentML

class TestGetDataAnalysisDerivTrendsExpansiveRecentML(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsExpansiveRecentML.ControllerGetDataAnalysisDerivTrendsExpansiveRecentML()

    async def TestGetDataAnalysisDerivTrendsExpansiveRecentML(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivTrendsExpansiveRecentML(request)

        print("controller:",result)