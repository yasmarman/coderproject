from django.db import models
from ckeditor.fields import RichTextField

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return f'{self.autor} {self.contenido}'