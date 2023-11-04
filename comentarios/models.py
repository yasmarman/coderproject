from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None) 
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
