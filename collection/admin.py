from django.contrib import admin
from collection.models import Pokemon

# Register your models here.


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_1', 'type_2', 'region')
    list_filter = ('type_1', 'type_2', 'region')
    ordering = ('id',)
admin.site.register(Pokemon, PokemonAdmin)
