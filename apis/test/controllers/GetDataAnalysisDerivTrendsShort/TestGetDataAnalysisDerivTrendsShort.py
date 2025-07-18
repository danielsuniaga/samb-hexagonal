import unittest

import apis.controllers.GetDataAnalysisDerivTrendsShort.GetDataAnalysisDerivTrendsShort as ControllerGetDataAnalysisDerivTrendsShort

class TestGetDataAnalysisDerivTrendsShort(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsShort.ControllerGetDataAnalysisDerivTrendsShort()

    async def TestGetDataAnalysisDerivTrendsShort(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivShort(request)

        print("controller:",result)