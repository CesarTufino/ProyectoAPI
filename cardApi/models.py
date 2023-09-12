from django.db import models


class Card(models.Model):
    id = models.CharField(primary_key=True,max_length=10) 
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    cost = models.IntegerField()

