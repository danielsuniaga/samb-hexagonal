# apis/urls.py
from django.urls import path
from .views import GetDataAnalysisDeriv, GetEndPoint, GetDailyReportEntrys,AddModels

urlpatterns = [
    path('get-data-analysis-deriv/', GetDataAnalysisDeriv.as_view(), name='get-data-analysis-deriv'),
    path('get-endpoint/', GetEndPoint.as_view(), name='get-endpoint'),
    path('get-daily-report-entrys/', GetDailyReportEntrys.as_view(), name='get-daily-report-entrys'),
    path('add-models/', AddModels.as_view(), name='add-models'),
]
