from django.db import models

class Tienda(models.Model):
    producto = models.CharField(max_length=20)
    descripcion= models.CharField(max_length=80)