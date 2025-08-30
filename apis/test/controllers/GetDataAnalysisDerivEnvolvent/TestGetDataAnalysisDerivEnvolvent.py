import unittest
import apis.controllers.GetDataAnalysisDerivEnvolvent.GetDataAnalysisDerivEnvolvent as ControllerGetDataAnalysisDerivEnvolvent

class TestGetDataAnalysisDerivEnvolvent(unittest.IsolatedAsyncioTestCase):
    controller = None

    def setUp(self):
        self.controller = ControllerGetDataAnalysisDerivEnvolvent.ControllerGetDataAnalysisDerivEnvolvent()

    async def test_GetDataAnalysisDerivEnvolvent(self):
        request = "test_request"
        result = await self.controller.GetDataAnalysisDerivEnvolvent(request)
        print("controller:", result)
