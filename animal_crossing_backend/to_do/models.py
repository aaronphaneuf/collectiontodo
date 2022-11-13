from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Collection(models.Model):
    FISH = "Fish"
    BUG = "Bug"
    SEA_CREATURE = "SeaCreature"
    CATEGORY_CHOICES = (FISH, "Fish"), (BUG, "Bug"), (SEA_CREATURE, "SeaCreature")
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='collections')
    season = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES,
                                default = 'Fish')
    image = models.CharField(max_length=255)



