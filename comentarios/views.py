from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .forms import ComentarioForm

@login_required
def ver_comentarios(request):
    comentarios = Comentario.objects.all()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentarios = form.save(commit=False)
            comentarios.user = request.user
            comentarios.save()
            return redirect('ver_comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/comentarios.html', {'comentarios': comentarios, 'form': form})



@login_required
def eliminar_comentario(request, id_comentario):

    comentario_a_eliminar = Comentario.objects.get(id=id_comentario)
    comentario_a_eliminar.delete()

    return redirect('ver_comentarios')



    

