from django.shortcuts import render
from django.views import generic

# cal/views.py

from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *


def home(request):
    return render(request, 'home/home.html')