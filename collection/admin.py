from django.contrib import admin
from collection.models import Pokemon

# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pokemon, PokemonAdmin)
