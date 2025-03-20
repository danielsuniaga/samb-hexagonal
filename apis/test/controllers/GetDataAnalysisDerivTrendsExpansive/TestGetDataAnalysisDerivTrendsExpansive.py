import unittest

import apis.controllers.GetDataAnalysisDerivTrendsExpansive.GetDataAnalysisDerivTrendsExpansive as ControllerGetDataAnalysisDerivTrendsExpansive

class TestGetDataAnalysisDerivTrendsExpansive(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsExpansive.ControllerGetDataAnalysisDerivTrendsExpansive()

    async def TestGetDataAnalysisDerivTrendsExpansive(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivExpansive(request)

        print("controller:",result)