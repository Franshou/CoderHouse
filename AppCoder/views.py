from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpRequest
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):
    return render (request, 'AppCoder/inicio.html')


def alumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {"alumnos" : alumnos}

    return render (request, "AppCoder/alumnos.html", contexto)

def docentes(request):
    docentes = Docente.objects.all()
    contexto = {"docentes" : docentes}

    return render (request, "AppCoder/docentes.html", contexto)

def cursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos" : cursos}

    return render (request, "AppCoder/cursos.html", contexto)


def abmAlumnos(request):
    if request.method == "POST":
        alumno = AlumnosForm(request.POST)

        if alumno.is_valid():

            informacion = alumno.cleaned_data
            data = Alumno( nombre = informacion['nombre'], apellido = informacion['apellido'], matricula = informacion['matricula'] )
            data.save()
            return render (request, 'AppCoder/inicio.html')

    else:
        alumnosFormulario = AlumnosForm()
        return render (request, 'AppCoder/abmAlumnos.html', {"alumnosFormulario" : alumnosFormulario})

def abmDocentes(request):
    if request.method == "POST":
        docente = DocentesForm(request.POST)

        if docente.is_valid():

            informacion = docente.cleaned_data
            data = Docente( nombre = informacion['nombre'], apellido = informacion['apellido'], catedra = informacion['catedra'] )
            data.save()
            return render (request, 'AppCoder/inicio.html')

    else:
        docentesFormulario = DocentesForm()
        return render (request, 'AppCoder/abmDocentes.html', {"docentesFormulario" : docentesFormulario})

def abmCursos(request):
    if request.method == "POST":
        curso = CursosForm(request.POST)

        if curso.is_valid():

            informacion = curso.cleaned_data
            data = Curso( comision = informacion['comision'], materia = informacion['materia'] )
            data.save()
            return render (request, 'AppCoder/inicio.html')

    else:
        cursosFormulario = CursosForm()
        return render (request, 'AppCoder/abmCursos.html', {"cursosFormulario" : cursosFormulario})

