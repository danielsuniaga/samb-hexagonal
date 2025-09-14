import unittest

from apis.controllers.GetDataAnalysisDerivPinBar.GetDataAnalysisDerivPinBar import ControllerGetDataAnalysisDerivPinBar
import apis.controllers.GetDataAnalysisDerivPinBarML.GetDataAnalysisDerivPinBarML as ControllerGetDataAnalysisDerivPinBarML

class TestGetDataAnalysisDerivPinBarML(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivPinBarML.ControllerGetDataAnalysisDerivPinBarML()

    async def TestGetDataAnalysisDerivPinBarML(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivPinBarML(request)

        print("controller:",result)