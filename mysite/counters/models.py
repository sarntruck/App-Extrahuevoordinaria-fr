from django.db import models

# Create your models here.
class Contador(models.Model):
    titulo=models.CharField(max_length=70)
    descripcion = models.TextField()
    valor = models.IntegerField(default=0)

    def __str__(self):
        return f"Llevas:{self.valor}"
    #boton = models.ManyToOneRel(models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE))