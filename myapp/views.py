from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template
from apps.models import Persona
from django.views.generic import ListView

def bienvenida(request):
    return HttpResponse('welcome jason')

def categoriaEdad(request, edad):
    if edad > 18:
        categoria = 'puede ingresar'
    else:
        categoria = 'menor de edad'
    resultado = '<h2>La categoria para la edad  %s</h2>' %categoria
    return HttpResponse(resultado)

def fecha(request):
    respuesta = '<h2>fecha actual {0}</h2>'.format(datetime.datetime.now().strftime('%A %d/%m/%Y %M:%S'))
    return HttpResponse(respuesta)


def index(request):
    with open('apps/template/index.html') as plantilla:
        archivo = Template(plantilla.read())
    contexto = Context()
    documento = archivo.render(contexto)
    return HttpResponse(documento)



def atajos(request):
    nombre = 'jason'
    fecha = datetime.datetime.now()
    lista = ['arya', 'blue']

    return render(request, 'parametros.html', {'user': nombre, 'fechaHoy': fecha, 'listas': lista})

def plantillaHija(request):
    return render(request, 'index2.html', {})

def index3(request):
    return render(request, 'index3.html', {})

def users(request):
    usuarios = Persona.objects.all()

    data = {
        'title': 'Pagina principal de views'
    }
    return render(request, 'index.html', {'users': usuarios})


class CusoListView(ListView):
    model = Persona
    template_name = 'index.html'