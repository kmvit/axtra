from django.urls import path
from .views import *


app_name='portfolio'

urlpatterns = [
    path('', CaselistView.as_view(), name='case_list'),
    path('<slug>/', CaseDetailView.as_view(), name='case_detail'),
    ]
