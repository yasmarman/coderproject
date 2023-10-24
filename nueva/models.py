from django.db import models
from ckeditor.fields import RichTextField

class Paleta (models.Model):
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    descripcion = RichTextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    

    def  __str__(self):
        return f'{self.titulo} {self.detalle}'
    
