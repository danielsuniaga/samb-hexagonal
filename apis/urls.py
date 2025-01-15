# apis/urls.py
from django.urls import path
from .views import GetDataAnalysisDeriv,GetEndPoint

urlpatterns = [

    path('get-data-analysis-deriv/', GetDataAnalysisDeriv.as_view()),
    path('get-endpoint/', GetEndPoint.as_view())
    
]
