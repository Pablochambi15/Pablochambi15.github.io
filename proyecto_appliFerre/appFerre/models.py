 
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        texto ="{0}-{1}-{2}-{3}"
        return texto.format(self.nombre,self.descripcion,self.precio,self.cantidad)
