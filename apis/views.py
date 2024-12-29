# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import apis.controllers.GetDataAnalysisDeriv.GetDataAnalysisDeriv as ControllerGetDataAnalysisDeriv

class GetDataAnalysisDeriv(APIView):

    controller = None

    def __init__(self):

        self.controller = ControllerGetDataAnalysisDeriv.ControllerGetDataAnalysisDeriv()

    def post(self, request, format=None):

        return Response(self.controller.GetDataAnalysisDeriv(request))
