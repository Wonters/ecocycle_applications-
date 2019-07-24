from django.db import models
from django.utils import timezone
from django.core.exceptions import *

import json


# Create your models here.

class Legume(models.Model):
    nom = models.CharField(max_length=200)
    date_plantation = models.DateTimeField(default=timezone.now)
    nbr_plant = models.IntegerField(default=0)
    poid_recolte = models.IntegerField(default=0)
    type = models.CharField(max_length=200)
    date_recolte = models.DateTimeField(default=timezone.now)

    def get_plantation(self):
        return {'date': self.date_plantation, 'nbr_plants': self.nbr_plant}

    def get_recolte(self):
        return {'date': self.date_recolte, 'poids': self.poid_recolte}

    def set_recolteDate(self, name, date):
        try:
            legum = Legume.objects.get(nom=name) # changer pour l'id
            legum.date_recolte = date

        except FieldError as error:
            print('legume {0} not exist'.format_map(name))
            print('error'.format_map(error))

    def __str__(self):
        return self.nom

    def getDb(self):
        dictLegum = {}
        listL = self.getListLegum()
        for nom in listL:
            ltanpon = []
            for legum in Legume.objects.all():
                if legum.nom == nom:
                    ltanpon.append(legum)
            dictLegum[nom] = ltanpon
        return dictLegum

    def getListLegum(self):
        listL = []
        db = Legume.objects.all()
        for legum in db:
            listL.append(legum.nom)
        listL = list(set(listL))
        return listL

    def getPlantation(self):
        listPlantation = self.getDb()
        plantation = {}
        for key, value in listPlantation.items():
            plantation[key] = 0
            for legum in value:
                plantation[key] += legum.nbr_plant
        return plantation

    def getRecolte(self):
        listrecolte = self.getDb()
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
        return recolte, recolte_month

    def getCalendar(self):
        calendarRecoltePlotly = []
        listLegum = self.getListLegum()
        llegum = []
        for leg in Legume.objects.all():
            llegum.append(leg.nom)
        for mois in range(1, 13):
            lplant = []
            for legum_i in Legume.objects.all():
                daterecolte = legum_i.date_recolte
                if daterecolte.month == mois:
                    lplant.append(legum_i.nbr_plant)
                else:
                    lplant.append('')
            calendarRecoltePlotly.append(lplant)
        calendarRecoltePlotly.insert(0, llegum)
        print(calendarRecoltePlotly)
        calendarJSON = json.dumps(calendarRecoltePlotly)
        return calendarJSON

