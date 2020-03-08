from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from apps.usuario.models import Departamento

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    fecha_nacido = models.DateField (verbose_name= 'Fecha de Nacimiento')
    direccion = models.CharField(max_length=80)
#    departamento = models.OneToOneField(Departamento, null=False, blank=False, on_delete=models.DO_NOTHING)
    localidad = models.CharField(max_length=30)
    telefono = models.IntegerField()
    f_creacion = models.DateTimeField(auto_now=True)
    f_modificado = models.DateTimeField (auto_now_add=True)


