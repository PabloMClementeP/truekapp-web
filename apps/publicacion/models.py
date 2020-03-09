from django.db import models
from apps.perfiles.models import Perfil

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=30)

	class Meta:
		ordering = ['nombre']
	
	def __str__(self):
		return self.nombre


class SubCategoria(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, null = False, blank = False, on_delete = models.CASCADE, related_name='tag')

    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    titulo = models.CharField (max_length=30)
    descripcion = models.CharField (max_length=500)
    categoria  = models.OneToOneField (Categoria, null = False, blank = False, on_delete = models.DO_NOTHING)
    subcategoria = models.OneToOneField (SubCategoria, null = False, blank = False, on_delete = models.DO_NOTHING)
    valor = models.IntegerField ()
    imagen = models.CharField (max_length=500)
    usuario = models.OneToOneField (Perfil, null = False, blank = False, on_delete = models.DO_NOTHING)
    cambia_por = models.ManyToManyField (SubCategoria, related_name='cambio')
    activo = models.BooleanField ()
    fecha_publicado = models.DateTimeField (auto_now= True)
    fecha_modificado = models.DateTimeField (auto_now=False, auto_now_add= True)

    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"


    def __str__(self):
        return self.titulo