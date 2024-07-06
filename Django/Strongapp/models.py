from django.db import models

# Create your models here.

class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50,null=False,blank=False)
    descripcion = models.TextField(null=False,blank=False)
    descripcion2 = models.TextField(null=False,blank=False)
    precio = models.IntegerField(null=False,blank=False)
    duracion = models.CharField(max_length=50,null=False,blank=False)
    incluye = models.TextField(null=False,blank=False)
    imagen = models.CharField(max_length=100,null=False,blank=False)

class Usuario(models.Model):
    email = models.EmailField(primary_key=True, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=20,null=False,blank=False)
    apellido = models.CharField(max_length=20,null=False,blank=False)
    contrasena = models.CharField(max_length=20,null=False,blank=False)



