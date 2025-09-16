# apis/urls.py
from django.urls import path
from .views import GetDataAnalysisDeriv, GetEndPoint, GetDailyReportEntrys,AddModels, GetDailyReportCrons, GetDataAnalysisDerivWMA, GetDataAnalysisDerivExpansive, SendDataSession, GetDataAnalysisDerivMinus, GetDataAnalysisDerivML,GetDataAnalysisDerivMinusML, GetDataAnalysisDerivWMAML, GetDataAnalysisDerivEnvolvent,GetDataAnalysisDerivRecent,GetDataAnalysisDerivWMARecent, GetDataAnalysisDerivMinusRecent, GetDataAnalysisDerivExpansiveRecent, GetDataAnalysisDerivPinbar,GetDataAnalysisDerivExpansiveML,GetDataAnalysisDerivEnvolventML, GetDataAnalysisDerivWMARecentML, GetDataAnalysisDerivPinBarML, GetDataAnalysisDerivRecentML

urlpatterns = [
    path('get-data-analysis-deriv-minus/', GetDataAnalysisDerivMinus.as_view(), name='get-data-analysis-deriv-minus'),
    path('get-data-analysis-deriv-minus-recent/', GetDataAnalysisDerivMinusRecent.as_view(), name='get-data-analysis-deriv-minus-recent'),
    path('get-data-analysis-deriv-minus-ml/', GetDataAnalysisDerivMinusML.as_view(), name='get-data-analysis-deriv-minus-ml'),
    path('get-data-analysis-deriv-expansive/', GetDataAnalysisDerivExpansive.as_view(), name='get-data-analysis-deriv-expansive'),
    path('get-data-analysis-deriv-expansive-ml/', GetDataAnalysisDerivExpansiveML.as_view(), name='get-data-analysis-deriv-expansive-ml'),
    path('get-data-analysis-deriv-expansive-recent/', GetDataAnalysisDerivExpansiveRecent.as_view(), name='get-data-analysis-deriv-expansive-recent'),
    path('get-data-analysis-deriv-wma/', GetDataAnalysisDerivWMA.as_view(), name='get-data-analysis-deriv-wma'),
    path('get-data-analysis-deriv-wma-recent/', GetDataAnalysisDerivWMARecent.as_view(), name='get-data-analysis-deriv-wma-recent'),
    path('get-data-analysis-deriv-wma-recent-ml/', GetDataAnalysisDerivWMARecentML.as_view(), name='get-data-analysis-deriv-wma-recent-ml'),
    path('get-data-analysis-deriv-wma-ml/', GetDataAnalysisDerivWMAML.as_view(), name='get-data-analysis-deriv-wma-ml'),
    path('get-data-analysis-deriv/', GetDataAnalysisDeriv.as_view(), name='get-data-analysis-deriv'),
    path('get-data-analysis-deriv-recent/', GetDataAnalysisDerivRecent.as_view(), name='get-data-analysis-deriv-recent'),
    path('get-data-analysis-deriv-recent-ml/', GetDataAnalysisDerivRecentML.as_view(), name='get-data-analysis-deriv-recent-ml'),
    path('get-data-analysis-deriv-ml/', GetDataAnalysisDerivML.as_view(), name='get-data-analysis-deriv-ml'),
    path('get-endpoint/', GetEndPoint.as_view(), name='get-endpoint'),
    path('get-daily-report-entrys/', GetDailyReportEntrys.as_view(), name='get-daily-report-entrys'),
    path('get-daily-report-crons/', GetDailyReportCrons.as_view(), name='get-daily-report-crons'),
    path('add-models/', AddModels.as_view(), name='add-models'),
    path('send-data-session/', SendDataSession.as_view(), name='send-data-session'),
    path('get-data-analysis-deriv-envolvent/', GetDataAnalysisDerivEnvolvent.as_view(), name='get-data-analysis-deriv-envolvent'),
    path('get-data-analysis-deriv-envolvent-ml/', GetDataAnalysisDerivEnvolventML.as_view(), name='get-data-analysis-deriv-envolvent-ml'),
    path('get-data-analysis-deriv-pinbar/', GetDataAnalysisDerivPinbar.as_view(), name='get-data-analysis-deriv-pinbar'),
    path('get-data-analysis-deriv-pinbar-ml/', GetDataAnalysisDerivPinBarML.as_view(), name='get-data-analysis-deriv-pinbar-ml'),
]
