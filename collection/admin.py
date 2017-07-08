from django.contrib import admin
from collection.models import Pokemon, Region, Type, Nature
# from collection.models import Trainer

# Register your models here.


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_1', 'type_2', 'region')
    list_filter = ('type_1', 'type_2', 'region')
    ordering = ('id',)
admin.site.register(Pokemon, PokemonAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
admin.site.register(Type, TypeAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
admin.site.register(Region, RegionAdmin)

class NatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'increase', 'decrease')
    ordering = ('id',)
admin.site.register(Nature, NatureAdmin)

# class TrainerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'region')
#     # list_filter = 'region'
#     ordering = ('id',)
# admin.site.register(Trainer, TrainerAdmin)

