from django.db import models
from django.utils import timezone


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

    def __str__(self):
        return self.nom