from http.client import HTTPResponse
from django.shortcuts import render
from .models import Cadena
from .models import Fecha
from .models import Partido

# Create your views here.

def cadena(request):
    cadena= Cadena(nombre= "cadena de texto", apellido="funcion escritura")
    cadena.save()
    documento= f"Cadena: {cadena.nombre} y apellido {cadena.apellido}"
    return HTTPResponse(documento)

def fecha(request):
    fecha= Fecha(evento= "asignatura lengua")
    fecha.save()
    dia= f"Fecha: {fecha.evento}"
    return HTTPResponse(dia)

def partido(request):
    partido= Partido(club= "Boca", cantidad_goles=2)
    partido.save()
    actual=f"Partido: {partido.club}, hubo {partido.cantidad_goles}"
    return HTTPResponse(actual)