from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AutoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class SubgenerosFormulario(forms.Form):
    subgenero = forms.CharField(max_length=15)
    editorial = forms.CharField(max_length=30)

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)


class RegistroUsuario(UserCreationForm):

    class Meta:
        model = User
        fields = ["username" , "first_name", "last_name", "email", "password1", "password2"]


class FormularioEditar(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]    

class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField()