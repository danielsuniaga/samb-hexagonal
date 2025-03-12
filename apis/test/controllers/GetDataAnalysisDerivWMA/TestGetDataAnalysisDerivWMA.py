import unittest

import apis.controllers.GetDataAnalysisDerivWMA.GetDataAnalysisDerivWMA as ControllerGetDataAnalysisDerivWMA    

class TestGetDataAnalysisDerivWMA(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivWMA.ControllerGetDataAnalysisDerivWMA()

    async def TestGetDataAnalysisDerivWMA(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivWMA(request)

        print("controller:",result)

