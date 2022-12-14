from django.db import models

# Create your models here.


class formArticulo(models.Model):
    titulo = models.CharField(max_length=128)
    fecha = models.DateField()
    creador = models.CharField(max_length=140)
    contenido = models.CharField(max_length=600)
    imagen = models.ImageField(upload_to="imagenart", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.creador}"
