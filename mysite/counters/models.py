from django.db import models

# Create your models here.
class Counter(models.Model):
    title=models.CharField(max_length=70)
    boost_recuso =models.TextField(max_length=70) #asociado al bono al contador que da el recurso
    num_recurso = models.TextField(max_length=70) #cuenta cuantas iteraciones del recurso hay comprado
    boton = models.CharField(max_length=3) #field temporal que sera el boton de compra

    def __str__(self):
        return (self.title,self.boost_recuso,self.num_recurso)
    