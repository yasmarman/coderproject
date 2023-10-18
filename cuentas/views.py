from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from cuentas.forms import NuestroFormularioDeRegistro
from django.contrib.auth import authenticate, login as django_login

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username= formulario.cleaned_data.get('username')
            password =formulario.cleaned_data.get('password')
            usuario= authenticate(username=username, password=password)
            django_login(request, usuario)
            return redirect('inicio')
    else: 
        formulario = AuthenticationForm()

    return render(request, 'cuentas/login.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario= NuestroFormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        
    else:
        formulario = NuestroFormularioDeRegistro()

    return render(request, 'cuentas/registro.html',{'formulario':formulario})