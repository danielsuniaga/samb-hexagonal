# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync

import apis.controllers.GetDataAnalysisDerivTrends.GetDataAnalysisDerivTrends as ControllerGetDataAnalysisDerivTrends
import apis.controllers.GetEndPoint.GetEndPoint as ControllerGetEndPoint
import apis.controllers.GetDailyReportEntrys.GetDailyReportEntrys as ControllerGetDailyReportEntrys
import apis.controllers.AddModels.AddModels as ControllerAddModels
import apis.controllers.GetDailyReportCrons.GetDailyReportCrons as ControllerGetDailyReportCrons
import apis.controllers.GetDataAnalysisDerivWMA.GetDataAnalysisDerivWMA as ControllerGetDataAnalysisDerivWMA    

class GetDataAnalysisDeriv(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrends.ControllerGetDataAnalysisDerivTrends()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDeriv(request)

        return result
    
class GetDataAnalysisDerivWMA(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivWMA.ControllerGetDataAnalysisDerivWMA()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivWMA(request)

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
    
class GetDailyReportCrons(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDailyReportCrons.ControllerGetDailyReportCrons()

    def post(self, request, format=None):

        result = self.controller.GetDailyReportCrons()

        return Response(result)
    
class AddModels(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerAddModels.ControllerAddModels()

    def post(self, request, format=None):

        result = self.controller.AddModels()

        return Response(result)
        