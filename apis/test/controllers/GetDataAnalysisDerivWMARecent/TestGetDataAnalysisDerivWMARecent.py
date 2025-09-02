import unittest

import apis.controllers.GetDataAnalysisDerivWMARecent.GetDataAnalysisDerivWMARecent as ControllerGetDataAnalysisDerivWMARecent

class TestGetDataAnalysisDerivWMARecent(unittest.IsolatedAsyncioTestCase):

    controller = None

    def setUp(self):

        self.controller = ControllerGetDataAnalysisDerivWMARecent.ControllerGetDataAnalysisDerivWMARecent()

    async def TestGetDataAnalysisDerivWMARecent(self):

        request = "4842ff1da2c8faefab30d9c36bdac82a641a9edbce8fcc604982a2e00846b55b"

        result = await self.controller.GetDataAnalysisDerivWMARecent(request)

        print("controller:",result)

