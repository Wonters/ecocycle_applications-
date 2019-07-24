from django.shortcuts import render

from tierlieu.models import *

## travailler sur la connexion des utilisateurs
def home(request):
    event = Event()
    event.geteventsToCome()
    return render(request, 'home/home.html')

