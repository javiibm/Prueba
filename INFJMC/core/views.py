from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carrera
from .models import Docente

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

def nueva_carrera(request):
    if request.POST:
        nombre= request.POST['nombre']
        c = Carrera(codigo=111,nombre=nombre,duracion=1)
        print("funciona")
        c.save()
        return redirect(carreras)
    return render(request, 'core/nueva_carrera.html')

def nuevo_docente(request):
    if request.POST:
        nombre= request.POST['nombre']
        apellido= request.POST['apellido']
        email= request.POST['email']
        d = Docente(nombre=nombre,apellido=apellido,email=email)
        d.save()
        return redirect(docentes)
    return render(request, 'core/nuevo_docente.html')