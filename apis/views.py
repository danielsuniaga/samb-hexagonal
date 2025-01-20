# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync


import apis.controllers.GetDataAnalysisDeriv.GetDataAnalysisDeriv as ControllerGetDataAnalysisDeriv
import apis.controllers.GetEndPoint.GetEndPoint as ControllerGetEndPoint

class GetDataAnalysisDeriv(APIView):
    """
    Async APIView for handling 'get-data-analysis-deriv' endpoint.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = ControllerGetDataAnalysisDeriv.ControllerGetDataAnalysisDeriv()

    async def post(self, request, format=None):
        try:
            # Call the async controller method
            result = await self.controller.GetDataAnalysisDeriv(request)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

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