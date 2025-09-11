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
import apis.controllers.GetDataAnalysisDerivEnvolvent.GetDataAnalysisDerivEnvolvent as ControllerGetDataAnalysisDerivEnvolvent
import apis.controllers.GetDataAnalysisDerivTrendsML.GetDataAnalysisDerivTrendsML as ControllerGetDataAnalysisDerivTrendsML
import apis.controllers.GetDataAnalysisDerivTrendsMinusML.GetDataAnalysisDerivTrendsMinusML as ControllerGetDataAnalysisDerivTrendsMinusML
import apis.controllers.GetDataAnalysisDerivWMAML.GetDataAnalysisDerivWMAML as ControllerGetDataAnalysisDerivWMAML
import apis.controllers.GetDataAnalysisDerivTrendsRecent.GetDataAnalysisDerivTrendsRecent as ControllerGetDataAnalysisDerivTrendRecent
import apis.controllers.GetDataAnalysisDerivWMARecent.GetDataAnalysisDerivWMARecent as ControllerGetDataAnalysisDerivWMARecent
import apis.controllers.GetDataAnalysisDerivTrendsMinusRecent.GetDataAnalysisDerivTrendsMinusRecent as ControllerGetDataAnalysisDerivTrendsMinusRecent
import apis.controllers.GetDataAnalysisDerivTrendsExpansiveRecent.GetDataAnalysisDerivTrendsExpansiveRecent as ControllerGetDataAnalysisDerivTrendsExpansiveRecent
import apis.controllers.GetDataAnalysisDerivTrendsExpansiveML.GetDataAnalysisDerivTrendsExpansiveML as ControllerGetDataAnalysisDerivTrendsExpansiveML
import apis.controllers.GetDataAnalysisDerivEnvolventML.GetDataAnalysisDerivEnvolventML as ControllerGetDataAnalysisDerivEnvolventML
import apis.controllers.GetDataAnalysisDerivPinBar.GetDataAnalysisDerivPinBar as ControllerGetDataAnalysisDerivPinBar

class GetDataAnalysisDerivEnvolvent(APIView):
    controller = None

    def __init__(self):
        self.controller = ControllerGetDataAnalysisDerivEnvolvent.ControllerGetDataAnalysisDerivEnvolvent()

    def post(self, request, format=None):
        response_data = async_to_sync(self.async_post)(request)
        return Response(response_data)

    async def async_post(self, request):
        result = await self.controller.GetDataAnalysisDerivEnvolvent(request)
        return result
    
class GetDataAnalysisDerivEnvolventML(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivEnvolventML.ControllerGetDataAnalysisDerivEnvolventML()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivEnvolventML(request)

        return result
    
class GetDataAnalysisDerivPinbar(APIView):
    controller = None

    def __init__(self):
        self.controller = ControllerGetDataAnalysisDerivPinBar.ControllerGetDataAnalysisDerivPinBar()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)
        return Response(response_data)

    async def async_post(self, request):
        result = await self.controller.GetDataAnalysisDerivPinBar(request)
        return result

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
    
class GetDataAnalysisDerivRecent(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendRecent.ControllerGetDataAnalysisDerivTrendRecent()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivRecent(request)

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
    
class GetDataAnalysisDerivExpansiveML(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsExpansiveML.ControllerGetDataAnalysisDerivTrendsExpansiveML()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivExpansiveML(request)

        return result
    
class GetDataAnalysisDerivExpansiveRecent(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsExpansiveRecent.ControllerGetDataAnalysisDerivTrendsExpansiveRecent()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivExpansiveRecent(request)

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
    
class GetDataAnalysisDerivMinusRecent(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivTrendsMinusRecent.ControllerGetDataAnalysisDerivTrendsMinusRecent()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)

    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivMinusRecent(request)

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
    
class GetDataAnalysisDerivWMARecent(APIView):

    controller = None

    def __init__(self):
        self.controller = ControllerGetDataAnalysisDerivWMARecent.ControllerGetDataAnalysisDerivWMARecent()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)

    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivWMARecent(request)

        return result
    
class GetDataAnalysisDerivWMARecentML(APIView):

    # controller = None

    # def __init__(self):
    #     self.controller = ControllerGetDataAnalysisDerivWMARecent.ControllerGetDataAnalysisDerivWMARecent()

    def post(self, request, format=None):

        return Response(True)

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)

    # async def async_post(self, request):

    #     result = await self.controller.GetDataAnalysisDerivWMARecent(request)

    #     return result
    
class GetDataAnalysisDerivWMAML(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDerivWMAML.ControllerGetDataAnalysisDerivWMAML()

    def post(self, request, format=None):

        response_data = async_to_sync(self.async_post)(request)

        return Response(response_data)
        
    async def async_post(self, request):

        result = await self.controller.GetDataAnalysisDerivWMAML(request)

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
        