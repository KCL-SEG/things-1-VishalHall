from django.db import models
from django.db.models import Model

class Model(Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    quantity = models.IntegerField()