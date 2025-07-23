# apis/urls.py
from django.urls import path
from .views import GetDataAnalysisDeriv, GetEndPoint, GetDailyReportEntrys,AddModels, GetDailyReportCrons, GetDataAnalysisDerivWMA, GetDataAnalysisDerivExpansive, SendDataSession, GetDataAnalysisDerivMinus

urlpatterns = [
    path('get-data-analysis-deriv-minus/', GetDataAnalysisDerivMinus.as_view(), name='get-data-analysis-deriv-minus'),
    path('get-data-analysis-deriv-expansive/', GetDataAnalysisDerivExpansive.as_view(), name='get-data-analysis-deriv-expansive'),
    path('get-data-analysis-deriv-wma/', GetDataAnalysisDerivWMA.as_view(), name='get-data-analysis-deriv-wma'),
    path('get-data-analysis-deriv/', GetDataAnalysisDeriv.as_view(), name='get-data-analysis-deriv'),
    path('get-endpoint/', GetEndPoint.as_view(), name='get-endpoint'),
    path('get-daily-report-entrys/', GetDailyReportEntrys.as_view(), name='get-daily-report-entrys'),
    path('get-daily-report-crons/', GetDailyReportCrons.as_view(), name='get-daily-report-crons'),
    path('add-models/', AddModels.as_view(), name='add-models'),
    path('send-data-session/', SendDataSession.as_view(), name='send-data-session'),
]
