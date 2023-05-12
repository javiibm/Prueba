from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hola Mundo</h1>")
    return render(request, 'core/index.html')


def carreras(request):
    carreras = Carrera.objects.all
    return render(request, 'core/carreras.html', {'carreras':carreras})

    #return HttpResponse("<h1>Carreras</h1>" + "<p>INGENIERIA DE EJECUCION EN MECANICA DE PROCESOS Y MANTENIMIENTO INDUSTRIAL<br> INGENIERIA EN FABRICACION Y DISEÑO INDUSTRIAL</p>")

def docentes(request):
    return render(request, 'core/docentes.html')

    #return HttpResponse("<h1>Docentes</h1>")

