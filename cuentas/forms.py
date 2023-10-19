from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class NuestroFormularioDeRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {campo: '' for campo in fields }

class NuestroFormularioEditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Email actual')
    first_name = forms.CharField( label='nombre', max_length=30)
    last_name = forms.CharField(label='apellido',max_length=50)
    link = forms.URLField(required=False)
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User 
        fields = ['email', 'first_name', 'last_name', 'link', 'avatar']