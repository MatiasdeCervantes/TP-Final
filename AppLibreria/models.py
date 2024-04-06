from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserChangeForm
# Create your models here.

class clientes(models.Model): 

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    def __str__(self):

        return f"{self.nombre}, {self.apellido}, {self.email}"


class subgeneros(models.Model):

    subgenero = models.CharField(max_length=15)
    editorial = models.CharField(max_length=30)
    def __str__(self):

        return f"{self.subgenero}, {self.editorial}"

class autor(models.Model):
    
    nombre = models.CharField(max_length=30)
    def __str__(self):

        return f"{self.nombre}"

class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


class EditarUsuario(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ["username", "email"]


