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
import apis.controllers.GetDataAnalysisDerivTrendsExpansive.GetDataAnalysisDerivTrendsExpansive as ControllerGetDataAnalysisDerivTrendsExpansive  
import apis.controllers.SendDataSession.SendDataSession as ControllerSendDataSession
import apis.controllers.GetDataAnalysisDerivTrendsMinus.GetDataAnalysisDerivTrendsMinus as ControllerGetDataAnalysisDerivTrendsMinus
import apis.controllers.GetDataAnalysisDerivTrendsML.GetDataAnalysisDerivTrendsML as ControllerGetDataAnalysisDerivTrendsML
import apis.controllers.GetDataAnalysisDerivTrendsMinusML.GetDataAnalysisDerivTrendsMinusML as ControllerGetDataAnalysisDerivTrendsMinusML

class SendDataSession(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerSendDataSession.ControllerSendDataSession() 

    def send_data(self):

        return self.controller.send_data()  

    def post(self, request, format=None):

        return Response(self.send_data())
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
    
class GetDataAnalysisDerivML(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsML.ControllerGetDataAnalysisDerivTrendsML()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivML(request)

        return result
    
class GetDataAnalysisDerivExpansive(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsExpansive.ControllerGetDataAnalysisDerivTrendsExpansive()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivExpansive(request)

        return result
    
class GetDataAnalysisDerivMinus(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsMinus.ControllerGetDataAnalysisDerivTrendsMinus()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)

    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivMinus(request)

        return result

class GetDataAnalysisDerivMinusML(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsMinusML.ControllerGetDataAnalysisDerivTrendsMinusML()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)

    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivMinusML(request)

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
        