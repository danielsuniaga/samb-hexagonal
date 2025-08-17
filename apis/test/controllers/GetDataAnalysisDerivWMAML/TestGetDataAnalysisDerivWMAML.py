import unittest

from apis.controllers.GetDataAnalysisDerivWMA.GetDataAnalysisDerivWMA import ControllerGetDataAnalysisDerivWMA
import apis.controllers.GetDataAnalysisDerivWMAML.GetDataAnalysisDerivWMAML as ControllerGetDataAnalysisDerivWMAML

class TestGetDataAnalysisDerivWMAML(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivWMAML.ControllerGetDataAnalysisDerivWMAML()

    async def TestGetDataAnalysisDerivWMAML(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivWMAML(request)

        print("controller:",result)

