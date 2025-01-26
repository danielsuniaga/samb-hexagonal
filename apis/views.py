# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync

import apis.controllers.GetDataAnalysisDeriv.GetDataAnalysisDeriv as ControllerGetDataAnalysisDeriv
import apis.controllers.GetEndPoint.GetEndPoint as ControllerGetEndPoint
import apis.controllers.GetDailyReportEntrys.GetDailyReportEntrys as ControllerGetDailyReportEntrys
import apis.controllers.AddModelRegressionLogistic.AddModelRegressionLogistic as ControllerAddModelRegressionLogistic

class GetDataAnalysisDeriv(APIView):

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDeriv.ControllerGetDataAnalysisDeriv()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDeriv(request)

        return result

class GetEndPoint(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetEndPoint.ControllerGetEndPoint()   

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)

    async def async_post(self, request):

        result = await self.controller.GetEndPoint()

        return result
    
class GetDailyReportEntrys(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDailyReportEntrys.ControllerGetDailyReportEntrys()   

    def post(self, request, format=None):

        result = self.controller.GetDailyReportEntrys()

        return Response(result)
    
class AddModelRegressionLogistic(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerAddModelRegressionLogistic.AddModelRegressionLogistic()

    def post(self, request, format=None):

        result = self.controller.AddModelRegressionLogistic(request)

        return Response(result)
        