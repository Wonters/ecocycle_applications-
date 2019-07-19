from django.shortcuts import render
from django.views import generic

# cal/views.py

from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from .models import *

## travailler sur la connexion des utilisateurs
def home(request):
    # session_key = request.session.session_key
    # print(request.session)
    # print(session_key)
    # print(Session.objects.all())
    # session = Session.objects.get(session_key=session_key)
    # session_data = session.get_decoded()
    # print(session_data)
    # uid = session_data.get('_auth_user_id')
    # user = User.objects.get(id=uid)
    # print(user)
    return render(request, 'home/home.html')

