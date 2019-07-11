from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
    dictLegum = getDb()
    return render(request, 'maraichage/home.html', {'list': dictLegum})


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

def culture(request):
    dictLegum = getDb()
    return render(request, 'maraichage/culture.html', {'Legums': dictLegum})


def addLegum(request):
    form = LegumeForm
    return render(request, 'maraichage/formAddLegum.html', {'form': form})


def saveLegum(request):
    form = LegumeForm(request.POST)
    form.save()
    listLegum = Legume.objects.all()
    return render(request, 'maraichage/home.html', {'listLegum': listLegum})


@csrf_exempt
def deleteLegum(request):
    if request.is_ajax():
        dict_ajax = dict(request.GET)
        name_LegToDel = dict_ajax['name'][0]
        print('delete {0}'.format(name_LegToDel))
        legum_to_delete = Legume.objects.filter(nom=name_LegToDel)
        legum_to_delete.delete()
    return culture(request)
