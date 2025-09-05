import unittest

import apis.controllers.GetDataAnalysisDerivPinBar.GetDataAnalysisDerivPinBar as ControllerGetDataAnalysisDerivPinBar

class TestGetDataAnalysisDerivPinBar(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivPinBar.ControllerGetDataAnalysisDerivPinBar()

    async def TestGetDataAnalysisDerivPinBar(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivPinBar(request)

        print("controller:",result)
