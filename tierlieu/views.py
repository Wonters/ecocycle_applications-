from django.shortcuts import render

# Create your views here.

from .models import *

def home(request):
    return render(request, 'tierlieu/home.html')


def adherents(request):
    users = User()
    listadherents = users._getlistUsers()
    print(listadherents[0]._meta.fields)
    return render(request, 'tierlieu/adherents.html', {'users':listadherents})