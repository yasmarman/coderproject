from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None) 
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
