from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'adhesion', 'status')

@admin.register(TypeAdhesion)
class TypeAdhesionAdmin(admin.ModelAdmin):
    list_display = ('type', 'prix')

@admin.register(Statu)
class StatuAdmin(admin.ModelAdmin):
    list_display = ('status', 'comp')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date', 'prix', 'abonnement')

admin.site.register(Adhesion)
admin.site.register(Machineoutil)
