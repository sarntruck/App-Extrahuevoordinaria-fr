from django.db import models

# Create your models here.
class Counter(models):
    nombre = models.CharField(max_length=70)
    contador = models.IntegerField()