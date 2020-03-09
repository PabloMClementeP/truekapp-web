from django.contrib import admin
from apps.publicacion.models import Categoria, SubCategoria, Publicacion

# Register your models here.
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    list_filter = ('categoria',)
    ordering = ('-titulo',)
    search_fields = ('titulo',)

class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria', 'nombre')
    ordering = ('categoria',)
    search_fields = ('categoria',)


admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Categoria)
admin.site.register(SubCategoria, SubCategoriaAdmin)
