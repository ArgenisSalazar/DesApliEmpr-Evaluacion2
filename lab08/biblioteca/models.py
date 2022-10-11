from email.policy import default
from os import fsdecode
from django.db import models

# Create your models here.
class Autor(models.Model):
    idAutor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Prestamos(models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    idLibro = models.CharField(max_length=10)
    idUsuario = models.CharField(max_length=10)
    FecPrestamo = models.DateField(null=False)
    FecDevolucion = models.DateField(null=False)
    
    def __str__(self):
        return self.idLibro
    
    class Meta:
        verbose_name="Prestamos"
        verbose_name_plural="Prestamos"

class Libro(models.Model):
    idLibro = models.AutoField(primary_key=True)
    codigo = models.IntegerField(default=0,null=False)
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    numpags = models.SmallIntegerField(default=0)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    prestamo = models.ManyToManyField(Prestamos)
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    numUsuario = models.IntegerField(default=0)
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    prestamo = models.ManyToManyField(Prestamos)
    
    def __str__(self):
        return self.nombre