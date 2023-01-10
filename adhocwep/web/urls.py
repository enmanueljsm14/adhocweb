from django.urls import path
from web.views import *

urlpatterns = [
    path('', contactcreateView.as_view(), name="webpaguina"),
    ]