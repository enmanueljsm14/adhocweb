from django.urls import path
from web.views import *

urlpatterns = [
    path('', weblistView.as_view(), name=""),
    ]