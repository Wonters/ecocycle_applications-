from django.contrib import admin

from .models import Legume


# Register your models here.



class LegumAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'date_plantation', 'nbr_plant', 'date_recolte', 'poid_recolte')
    search_fields = ('nom',)
    list_filter = ('date_plantation','date_recolte')

admin.site.register(Legume, LegumAdmin)
