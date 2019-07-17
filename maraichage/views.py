from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
from .forms import LegumeForm
from .models import Legume


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
    return render(request, 'maraichage/home.html', {'list': getDb(), 'plantation': json.dumps(getPlantation())})


def getDb():
    listL = []
    dictLegum = {}
    db = Legume.objects.all()
    for legum in db:
        listL.append(legum.nom)
    listL = list(set(listL))
    for nom in listL:
        ltanpon = []
        for legum in db:
            if legum.nom == nom:
                ltanpon.append(legum)
        dictLegum[nom] = ltanpon
    return dictLegum

def getPlantation():
    listPlantation = getDb()
    plantation = {}
    for key, value in listPlantation.items():
        plantation[key]=0
        for legum in value:
            plantation[key] += legum.nbr_plant
    return plantation

def getRecolte():
    listrecolte = getDb()
    recolte = {}
    recolte_month = {}
    for key, value in listrecolte.items():
        recolte[key] = {}
        recolte_month[key] = {}
        for legum in value:
            recolte[key][str(legum.date_recolte.year) + '-' + str(legum.date_recolte.month) + '-' + str(
                legum.date_recolte.day) + '-' + str(legum.date_recolte.hour)] = legum.poid_recolte
            recolte_month[key][str(legum.date_recolte.month)] = 0
    for key, value in listrecolte.items():
        for legum in value:
            recolte_month[key][str(legum.date_recolte.month)] += legum.poid_recolte
    print(recolte_month, recolte)
    return recolte, recolte_month


def culture(request):
    return render(request, 'maraichage/culture.html', {'Legums': getDb()})


def recolte(request):
    return render(request, 'maraichage/recolte.html', {'listLegum': getDb(), 'recolte': json.dumps(getRecolte()[0])})


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
