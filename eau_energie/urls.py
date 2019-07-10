from django.urls import path

from django.urls import include, path
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', home),
]
