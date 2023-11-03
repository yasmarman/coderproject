from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required

@login_required
def ver_comentarios(request):
    comentarios = Comentario.objects.all()
    form = ComentarioForm()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_comentarios')

    return render(request, 'comentarios/comentarios.html', {'comentarios': comentarios, 'form': form})