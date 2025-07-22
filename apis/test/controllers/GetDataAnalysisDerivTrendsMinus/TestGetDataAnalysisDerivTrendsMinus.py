import unittest

import apis.controllers.GetDataAnalysisDerivTrendsMinus.GetDataAnalysisDerivTrendsMinus as ControllerGetDataAnalysisDerivTrendsMinus

class TestGetDataAnalysisDerivTrendsMinus(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsMinus.ControllerGetDataAnalysisDerivTrendsMinus()

    async def TestGetDataAnalysisDerivTrendsMinus(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivMinus(request)

        print("controller:",result)