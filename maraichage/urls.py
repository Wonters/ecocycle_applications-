from django.urls import path

from django.urls import include, path
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', home),
    path('culture', culture),
    path('add', addLegum),
    path('save', saveLegum),
    #path('delete', deleteLegum),
    path('recolte', recolte),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
