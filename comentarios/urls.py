from django.urls import path
from comentarios.views import ver_comentarios, eliminar_comentario
urlpatterns = [
    path('ver_comentarios/', ver_comentarios, name='ver_comentarios'),
    path('eliminar_comentario/<int:id_comentario>/eliminar/', eliminar_comentario, name='eliminar_comentario'),
    
]