# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync
from django.db import close_old_connections
import gc

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
import apis.controllers.GetDataAnalysisDerivTrendsRecentML.GetDataAnalysisDerivTrendsRecentML as ControllerGetDataAnalysisDerivTrendsRecentML
import apis.controllers.GetDataAnalysisDerivWMARecent.GetDataAnalysisDerivWMARecent as ControllerGetDataAnalysisDerivWMARecent
import apis.controllers.GetDataAnalysisDerivTrendsMinusRecent.GetDataAnalysisDerivTrendsMinusRecent as ControllerGetDataAnalysisDerivTrendsMinusRecent
import apis.controllers.GetDataAnalysisDerivTrendsMinusRecentML.GetDataAnalysisDerivTrendsMinusRecentML as ControllerGetDataAnalysisDerivTrendsMinusRecentML
import apis.controllers.GetDataAnalysisDerivTrendsExpansiveRecent.GetDataAnalysisDerivTrendsExpansiveRecent as ControllerGetDataAnalysisDerivTrendsExpansiveRecent
import apis.controllers.GetDataAnalysisDerivTrendsExpansiveRecentML.GetDataAnalysisDerivTrendsExpansiveRecentML as ControllerGetDataAnalysisDerivTrendsExpansiveRecentML
import apis.controllers.GetDataAnalysisDerivTrendsExpansiveML.GetDataAnalysisDerivTrendsExpansiveML as ControllerGetDataAnalysisDerivTrendsExpansiveML
import apis.controllers.GetDataAnalysisDerivEnvolventML.GetDataAnalysisDerivEnvolventML as ControllerGetDataAnalysisDerivEnvolventML
import apis.controllers.GetDataAnalysisDerivWMARecentML.GetDataAnalysisDerivWMARecentML as ControllerGetDataAnalysisDerivWMARecentML
import apis.controllers.GetDataAnalysisDerivPinBar.GetDataAnalysisDerivPinBar as ControllerGetDataAnalysisDerivPinBar
import apis.controllers.GetDataAnalysisDerivPinBarML.GetDataAnalysisDerivPinBarML as ControllerGetDataAnalysisDerivPinBarML

class GetDataAnalysisDerivEnvolvent(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivEnvolvent.ControllerGetDataAnalysisDerivEnvolvent()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivEnvolvent(request)
        return result
    
class GetDataAnalysisDerivEnvolventML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivEnvolventML.ControllerGetDataAnalysisDerivEnvolventML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivEnvolventML(request)
        return result
    
class GetDataAnalysisDerivPinbar(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivPinBar.ControllerGetDataAnalysisDerivPinBar()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivPinBar(request)
        return result

class SendDataSession(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerSendDataSession.ControllerSendDataSession()
            result = controller.send_data()
            return Response(result)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()


class GetDataAnalysisDeriv(APIView):
    """✅ Controller se crea por request para evitar problemas de cursores DB cerrados"""

    def post(self, request, format=None):
        controller = None
        try:
            # ✅ Limpiar conexiones DB viejas
            close_old_connections()
            
            # ✅ Crear controller nuevo para este request
            controller = ControllerGetDataAnalysisDerivTrends.ControllerGetDataAnalysisDerivTrends()
            
            # ✅ Ejecutar lógica async
            response_data = async_to_sync(self.async_post)(request, controller)
            
            return Response(response_data)
            
        finally:
            # ✅ Limpieza explícita del controller y sus recursos
            if controller:
                del controller
            
            # ✅ Limpiar conexiones después del request
            close_old_connections()
            
            # ✅ Forzar recolección de basura

            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDeriv(request)
        return result
    
class GetDataAnalysisDerivRecent(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendRecent.ControllerGetDataAnalysisDerivTrendRecent()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivRecent(request)
        return result
    
class GetDataAnalysisDerivTrendsRecentML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsRecentML.ControllerGetDataAnalysisDerivTrendsRecentML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivTrendsRecentML(request)
        return result
    
class GetDataAnalysisDerivML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsML.ControllerGetDataAnalysisDerivTrendsML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivML(request)
        return result
    
class GetDataAnalysisDerivExpansive(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsExpansive.ControllerGetDataAnalysisDerivTrendsExpansive()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivExpansive(request)
        return result
    
class GetDataAnalysisDerivExpansiveML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsExpansiveML.ControllerGetDataAnalysisDerivTrendsExpansiveML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivExpansiveML(request)
        return result
    
class GetDataAnalysisDerivExpansiveRecent(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsExpansiveRecent.ControllerGetDataAnalysisDerivTrendsExpansiveRecent()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivExpansiveRecent(request)
        return result
    
class GetDataAnalysisDerivMinus(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsMinus.ControllerGetDataAnalysisDerivTrendsMinus()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivMinus(request)
        return result

class GetDataAnalysisDerivMinusRecent(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsMinusRecent.ControllerGetDataAnalysisDerivTrendsMinusRecent()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivMinusRecent(request)
        return result
    
class GetDataAnalysisDerivMinusRecentML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsMinusRecentML.ControllerGetDataAnalysisDerivTrendsMinusRecentML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivTrendsMinusRecentML(request)
        return result

class GetDataAnalysisDerivMinusML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsMinusML.ControllerGetDataAnalysisDerivTrendsMinusML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivMinusML(request)
        return result

class GetDataAnalysisDerivWMARecent(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivWMARecent.ControllerGetDataAnalysisDerivWMARecent()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivWMARecent(request)
        return result
    
class GetDataAnalysisDerivExpansiveRecentML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsExpansiveRecentML.ControllerGetDataAnalysisDerivTrendsExpansiveRecentML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivExpansiveRecentML(request)
        return result

class GetEndPoint(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetEndPoint.ControllerGetEndPoint()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetEndPoint()
        return result
    
class GetDailyReportEntrys(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDailyReportEntrys.ControllerGetDailyReportEntrys()
            result = controller.GetDailyReportEntrys()
            return Response(result)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
    
class GetDailyReportCrons(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDailyReportCrons.ControllerGetDailyReportCrons()
            result = controller.GetDailyReportCrons()
            return Response(result)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
    
class AddModels(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerAddModels.ControllerAddModels()
            result = controller.AddModels()
            return Response(result)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

class GetDataAnalysisDerivWMARecentML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivWMARecentML.ControllerGetDataAnalysisDerivWMARecentML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivWMARecentML(request)
        return result

class GetDataAnalysisDerivPinBarML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivPinBarML.ControllerGetDataAnalysisDerivPinBarML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivPinBarML(request)
        return result

class GetDataAnalysisDerivTrendsExpansiveRecentML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivTrendsExpansiveRecentML.ControllerGetDataAnalysisDerivTrendsExpansiveRecentML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivTrendsExpansiveRecentML(request)
        return result

class GetDataAnalysisDerivWMA(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivWMA.ControllerGetDataAnalysisDerivWMA()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()
        
    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivWMA(request)
        return result

class GetDataAnalysisDerivWMAML(APIView):
    """✅ Optimizado: Limpieza de memoria y conexiones DB"""

    def post(self, request, format=None):
        controller = None
        try:
            close_old_connections()
            controller = ControllerGetDataAnalysisDerivWMAML.ControllerGetDataAnalysisDerivWMAML()
            response_data = async_to_sync(self.async_post)(request, controller)
            return Response(response_data)
        finally:
            if controller:
                del controller
            close_old_connections()
            gc.collect()

    async def async_post(self, request, controller):
        result = await controller.GetDataAnalysisDerivWMAML(request)
        return result
        