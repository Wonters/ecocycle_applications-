from django.db import models

# Create your models here.

class TypeAdhesion(models.Model):
    type = models.CharField(max_length=50)
    prix = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.type


class Adhesion(models.Model):
    adhesion = models.ForeignKey(TypeAdhesion, on_delete=models.CASCADE)
    datesouscription = models.DateField()
    dateexpiration = models.DateField()

    def __str__(self):
        return self.adhesion.type

class Statu(models.Model):
    status = models.CharField(max_length=30)
    comp = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class User(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=200)
    mail = models.EmailField()
    adhesion = models.ForeignKey(Adhesion, on_delete=models.CASCADE)
    status = models.ForeignKey(Statu, on_delete=models.CASCADE)

    def __str__(self):
        return self.lastname

    def _getlistUsersName(self):
        db = User.objects.all()
        listusers = []
        for user in db:
            listusers.append(user.nom)
        return listusers

    def _getlistUsers(self):
        db = User.objects.all()
        return db


class Event(models.Model):
    nom = models.CharField(max_length=200)
    date = models.DateField()
    prix = models.IntegerField()
    abonnement = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Maintenance(models.Model):
    dateachat = models.DateField()
    prixachat = models.IntegerField()
    etat = models.BooleanField()

class Machineoutil(models.Model):
    nom = models.CharField(max_length=20)
    occupe = models.BooleanField()
    couthoraire = models.IntegerField()
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    def _getParcMachine(self):
        db = Machineoutil.objects.all()
        listmachines = []
        for machine in db:
            listmachines.append(machine.nom)
        return listmachines







