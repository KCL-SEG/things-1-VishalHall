from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(Model):
    name = models.CharField(
        max_length=30, 
        unique=True, 
        blank=False
    )
    description = models.CharField(
        max_length=120,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
    quantity = models.IntegerField()