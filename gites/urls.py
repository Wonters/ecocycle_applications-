from django.urls import path

from django.urls import include, path
from .views import *


urlpatterns = [
    path('', home),
]
