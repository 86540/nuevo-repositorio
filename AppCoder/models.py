from django.db import models

# Create your models here.

class Cadena(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)

class Fecha(models.Model):
    evento=models.CharField(max_length=40)
    

class Partido(models.Model):
    club=models.CharField(max_length=40)
    cantidad_goles=models.CharField(max_length=40)
    

