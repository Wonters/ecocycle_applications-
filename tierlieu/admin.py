from django.contrib import admin

# Register your models here.

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'adhesionuser', 'status')

class TypeAdhesionAdmin(admin.ModelAdmin):
    list_display = ('type', 'prix')

class StatuAdmin(admin.ModelAdmin):
    list_display =  ('status','comp')

admin.site.register(User, UserAdmin)

admin.site.register(Adhesion)
admin.site.register(Event)
admin.site.register(Machineoutil)
admin.site.register(TypeAdhesion, TypeAdhesionAdmin)
admin.site.register(Statu, StatuAdmin)