from django.db import models

# Create your models here.
class Counter(models.Model):
    nombre = models.CharField(max_length=75)
