from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Region(models.Model):
    KANTO = 'Kanto'
    JOHTO = 'Johto'
    HOENN = 'Hoenn'
    SINNOH = 'Sinnoh'
    UNOVA = 'Unova'
    KALOS = 'Kalos'
    ALOLA = 'Alola'

    REGION_CHOICES = (
        (KANTO, 'Kanto'),
        (JOHTO, 'Johto'),
        (HOENN, 'Hoenn'),
        (SINNOH, 'Sinnoh'),
        (UNOVA, 'Unova'),
        (KALOS, 'Kalos'),
        (ALOLA, 'Alola')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, choices=REGION_CHOICES, default=KANTO)
    # region = models.CharField(max_length=50, choices=REGION_CHOICES, default=KANTO)

    def __str__(self):
        return self.name


class Nature(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    increase = models.CharField(max_length=50, blank=True)
    decrease = models.CharField(max_length=50, blank=True)

class Type(models.Model):
    NORMAL = 'Normal'
    FIGHTING = 'Fighting'
    FLYING = 'Flying'
    POISON = 'Poison'
    GROUND = 'Ground'
    ROCK = 'Rock'
    BUG = 'Bug'
    GHOST = 'Ghost'
    STEEL = 'Steel'
    FIRE = 'Fire'
    WATER = 'Water'
    GRASS = 'Grass'
    ELECTRIC = 'Electric'
    PSYCHIC = 'Psychic'
    ICE = 'Ice'
    DRAGON = 'Dragon'
    DARK = 'Dark'
    FAIRY = 'Fairy'


    TYPE_CHOICES = (
        (NORMAL, 'Normal'),
        (FIGHTING, 'Fighting'),
        (FLYING, 'Flying'),
        (POISON, 'Poison'),
        (GROUND, 'Ground'),
        (ROCK, 'Rock'),
        (BUG, 'Bug'),
        (GHOST, 'Ghost'),
        (STEEL, 'Steel'),
        (FIRE, 'Fire'),
        (WATER, 'Water'),
        (GRASS, 'Grass'),
        (ELECTRIC, 'Electric'),
        (PSYCHIC, 'Psychic'),
        (ICE, 'Ice'),
        (DRAGON, 'Dragon'),
        (DARK, 'Dark'),
        (FAIRY, 'Fairy')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, choices=TYPE_CHOICES, default=NORMAL)


class Pokemon(models.Model):
    KANTO = 'Kanto'
    JOHTO = 'Johto'
    HOENN = 'Hoenn'
    SINNOH = 'Sinnoh'
    UNOVA = 'Unova'
    KALOS = 'Kalos'
    ALOLA = 'Alola'

    REGION_CHOICES = (
        (KANTO, 'Kanto'),
        (JOHTO, 'Johto'),
        (HOENN, 'Hoenn'),
        (SINNOH, 'Sinnoh'),
        (UNOVA, 'Unova'),
        (KALOS, 'Kalos'),
        (ALOLA, 'Alola')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type_1 = models.CharField(max_length=20)
    type_2 = models.CharField(max_length=20, blank=True)
    # region = models.CharField(max_length=50, choices=REGION_CHOICES, default=KANTO)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        # primary_key=True,
    )

    def __str__(self):
        return self.name


# class Trainer(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     hometown = models.CharField(max_length=127)
#     # champion = models.BooleanField(default=False)
#     # region = models.CharField(max_length=50, choices=REGION_CHOICES, default=KANTO)
#     # region = models.ForeignKey(
#     #     Region,
#     #     on_delete=models.CASCADE,
#     #     # primary_key=False,
#     # )


'''
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