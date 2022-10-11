from django.contrib import admin

# Register your models here.
from .models import Autor,Prestamos,Libro,Usuario

class AutorAdmin(admin.ModelAdmin):
    list_display=("idAutor","nombre","nacionalidad")
    search_fields=("idAutor","nombre")
    
class PrestamosAdmin(admin.ModelAdmin):
    list_display=("idPrestamo","idLibro","idUsuario","FecPrestamo","FecDevolucion")
    search_fields=("idPrestamo","idLibro")
    
class LibroAdmin(admin.ModelAdmin):
    list_display=("idLibro","codigo","titulo","isbn","editorial","numpags","autor")
    search_fields=("idLibro","codigo")
    
class UsuarioAdmin(admin.ModelAdmin):
    list_display=("idUsuario","numUsuario","nif","nombre","direccion","telefono")
    search_fields=("idUsuario","idUsuario")

admin.site.register(Autor,AutorAdmin)
admin.site.register(Prestamos,PrestamosAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Usuario,UsuarioAdmin)