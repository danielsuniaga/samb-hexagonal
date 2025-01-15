# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import apis.controllers.GetDataAnalysisDeriv.GetDataAnalysisDeriv as ControllerGetDataAnalysisDeriv
import apis.controllers.GetEndPoint.GetEndPoint as ControllerGetEndPoint

class GetDataAnalysisDeriv(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDeriv.ControllerGetDataAnalysisDeriv()

    async def post(self, request, format=None):

        result = await self.controller.GetDataAnalysisDeriv(request)

        return Response(result)
    
class GetEndPoint(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetEndPoint.ControllerGetEndPoint()

    def post(self, request, format=None):

        result = self.controller.GetEndPoint()
        
        return Response(result)
