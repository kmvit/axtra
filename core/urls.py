from django.urls import path, include

from core.views import HomePage, PageView

app_name='core'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<slug>/', PageView.as_view(), name='page'),
]
