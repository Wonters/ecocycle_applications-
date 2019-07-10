from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'eau_energie/home.html')