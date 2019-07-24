from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
from .forms import LegumeForm
from .models import Legume

def home(request):
    legume = Legume()
    return render(request, 'maraichage/home.html', {'list': legume.getDb(), 'plantation': json.dumps(legume.getPlantation()), 'calendar':legume.getCalendar()})

def culture(request):
    legume = Legume()
    return render(request, 'maraichage/culture.html', {'Legums': legume.getDb()})


def recolte(request):
    legume = Legume()
    return render(request, 'maraichage/recolte.html', {'listLegum': legume.getDb(), 'recolte': json.dumps(legume.getRecolte()[0])})


def addLegum(request):
    form = LegumeForm
    return render(request, 'maraichage/formAddLegum.html', {'form': form})


def saveLegum(request):
    form = LegumeForm(request.POST)
    form.save()
    return home(request)

@csrf_exempt
def deleteLegum(request):
    if request.is_ajax():
        dict_ajax = dict(request.GET)
        name_LegToDel = dict_ajax['name'][0]
        print('delete {0}'.format(name_LegToDel))
        legum_to_delete = Legume.objects.filter(nom=name_LegToDel)
        legum_to_delete.delete()
    return culture(request)
