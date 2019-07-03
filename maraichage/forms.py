from django.forms import ModelForm

from .models import Legume


class LegumeForm(ModelForm):
    class Meta:
        model = Legume
        fields = ('nom', 'date_plantation', 'nbr_plant', 'poid_recolte', 'type', 'date_recolte')
