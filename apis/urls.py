# apis/urls.py
from django.urls import path
from .views import GetDataAnalysisDeriv

urlpatterns = [

    path('get-data-analysis-deriv/', GetDataAnalysisDeriv.as_view())
    
]
