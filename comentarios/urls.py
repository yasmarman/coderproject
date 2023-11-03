from django.urls import path
from comentarios.views import ver_comentarios
urlpatterns = [
    path('ver_comentarios/', ver_comentarios, name='ver_comentarios'),
    # Otras rutas de tu aplicación
]