import unittest

import apis.controllers.GetDataAnalysisDerivTrendsExpansiveRecent.GetDataAnalysisDerivTrendsExpansiveRecent as ControllerGetDataAnalysisDerivTrendsExpansiveRecent

class TestGetDataAnalysisDerivTrendsExpansiveRecent(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsExpansiveRecent.ControllerGetDataAnalysisDerivTrendsExpansiveRecent()

    async def TestGetDataAnalysisDerivTrendsExpansiveRecent(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivExpansiveRecent(request)

        print("controller:",result)