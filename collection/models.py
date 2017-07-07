from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type_1 = models.CharField(max_length=20)
    type_2 = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.name

'''
class Trainer(models.Model):
    id = models.IntegerField(max_length=7)
    name = models.CharField(max_length=50)
    hometown = models.CharField(max_length=127)
    region = models.CharField(max_length=50)


class Team(models.Model):
    id = models.IntegerField(max_length=8)
    name = models.CharField(max_length=50)
    pokemon_01 = models.CharField(max_length=50)
    pokemon_02 = models.CharField(max_length=50)
    pokemon_03 = models.CharField(max_length=50)
    pokemon_04 = models.CharField(max_length=50)
    pokemon_05 = models.CharField(max_length=50)
    pokemon_06 = models.CharField(max_length=50)
'''