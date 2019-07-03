from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from .models import Legume
from .forms import LegumeForm
# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


def home(request):
    listLegum = Legume.objects.all()
    return render(request, 'maraichage/home.html', {'listLegum': listLegum})

def addLegum(request):
    form = LegumeForm
    return render(request, 'maraichage/formAddLegum.html', {'form': form})

def saveLegum(request):
    form = LegumeForm(request.POST)
    form.save()
    listLegum = Legume.objects.all()
    return render(request, 'maraichage/home.html', {'listLegum': listLegum})