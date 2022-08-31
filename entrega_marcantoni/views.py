from datetime import datetime
from tempfile import template
from xmlrpc.client import DateTime
from django.http import HttpResponse
from django.template import Template, Context

def nombre(request):
    return HttpResponse ("Mi hermana se llama Sonia")

def segundo(request):
    return HttpResponse("<br><br>, me llamo alejo")

def segundo_nombre(self, nombre1):
    documento=f"mi segundo nombre es: <br><br> {nombre1}"
    return HttpResponse(documento)

def primertemplate(request):
    nombres_de_mi_papa="Jose"
    profesion="encargado de edificio"
    lista_de_materias= ["historia","matematica","lengua"]
    diccionario={"nombre": nombres_de_mi_papa, "trabajo":profesion, "materias": lista_de_materias}
    mihtml= open("C:/Users/alejo/Desktop/nueva entrega/entrega_marcantoni/entrega_marcantoni/plantillas/template1.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    mi_contexto=Context(diccionario)
    documento=plantilla.render(mi_contexto)

    return HttpResponse(documento)