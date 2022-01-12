from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpRequest

from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.
from django.contrib.auth.decorators import login_required

def setAvatar(request):
    if request.user.is_authenticated:

        avatares = Avatar.objects.filter(user = request.user.id)

        x = len(avatares)

        if (x >= 1):
            y = x-1
            return avatares[y].imagen.url
        
        else:
            avatares = "https://i.ibb.co/6bGp6ZQ/blank.png"
            return avatares

    else:
        pass


def inicio(request):

    avatar = setAvatar(request)

    return render (request, "AppCoder/inicio.html", {"url" : avatar})


def about(request):

    avatar = setAvatar(request)

    return render (request, "AppCoder/about.html", {"url" : avatar})


@login_required
def alumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {"alumnos" : alumnos}

    avatar = setAvatar(request)

    return render (request, "AppCoder/alumnos.html", {"contexto" : contexto, "url" : avatar})

@login_required
def docentes(request):
    docentes = Docente.objects.all()
    contexto = {"docentes" : docentes}

    avatar = setAvatar(request)

    return render (request, "AppCoder/docentes.html", {"contexto" : contexto, "url" : avatar})

@login_required
def cursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos" : cursos}

    avatar = setAvatar(request)
    
    return render (request, "AppCoder/cursos.html", {"contexto" : contexto, "url" : avatar})

@login_required
def abmAlumnos(request):
    avatar = setAvatar(request)

    if request.method == "POST":
        alumno = AlumnosForm(request.POST)

        if alumno.is_valid():

            informacion = alumno.cleaned_data
            data = Alumno( nombre = informacion['nombre'], apellido = informacion['apellido'], matricula = informacion['matricula'] )
            data.save()
            return render (request, 'AppCoder/alumnos.html', {"url" : avatar})

    else:
        alumnosFormulario = AlumnosForm()
        return render (request, 'AppCoder/abmAlumnos.html', {"alumnosFormulario" : alumnosFormulario, "url" : avatar})

@login_required
def abmDocentes(request):
    avatar = setAvatar(request)

    if request.method == "POST":
        docente = DocentesForm(request.POST)

        if docente.is_valid():

            informacion = docente.cleaned_data
            data = Docente( nombre = informacion['nombre'], apellido = informacion['apellido'], catedra = informacion['catedra'] )
            data.save()
            return render (request, 'AppCoder/docentes.html', {"url" : avatar})

    else:
        docentesFormulario = DocentesForm()
        return render (request, 'AppCoder/abmDocentes.html', {"docentesFormulario" : docentesFormulario, "url" : avatar})

@login_required
def abmCursos(request):
    avatar = setAvatar(request)

    if request.method == "POST":
        curso = CursosForm(request.POST)

        if curso.is_valid():

            informacion = curso.cleaned_data
            data = Curso( comision = informacion['comision'], materia = informacion['materia'] )
            data.save()
            return render (request, 'AppCoder/cursos.html', {"url" : avatar})

    else:
        cursosFormulario = CursosForm()
        return render (request, 'AppCoder/abmCursos.html', {"cursosFormulario" : cursosFormulario, "url" : avatar})


#CBV
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls.base import reverse_lazy

class AlumnoList(ListView):
    model = Alumno
    template_name = "AppCoder/alumnos_list.html"

class AlumnoDetail(DetailView):
    model = Alumno
    template_name = "AppCoder/alumno_detail.html"

class AlumnoCreate(CreateView):
    model = Alumno
    success_url = "../alumnos/list"
    fields = ["nombre", "apellido", "matricula"]

class AlumnoUpdate(UpdateView):
    model = Alumno
    success_url = "../alumnos/list"
    fields = ["nombre", "apellido", "matricula"]

class AlumnoDelete(DeleteView):
    model = Alumno
    success_url = "../alumnos/list"


class DocenteList(ListView):
    model = Docente
    template_name = "AppCoder/docentes_list.html"

class DocenteDetail(DetailView):
    model = Docente
    template_name = "AppCoder/docente_detail.html"

class DocenteCreate(CreateView):
    model = Docente
    success_url = "../docentes/list"
    fields = ["nombre", "apellido", "catedra"]

class DocenteUpdate(UpdateView):
    model = Docente
    success_url = "../docentes/list"
    fields = ["nombre", "apellido", "catedra"]

class DocenteDelete(DeleteView):
    model = Docente
    success_url = "../docentes/list"


class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_list.html"

class CursoDetail(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detail.html"

class CursoCreate(CreateView):
    model = Curso
    success_url = "../cursos/list"
    fields = ["comision", "materia"]

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "../cursos/list"
    fields = ["comision", "materia"]

class CursoDelete(DeleteView):
    model = Curso
    success_url = "../cursos/list"


# LOGIN

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    avatar = setAvatar(request)

    if request.method == "POST":   
        loginForm = AuthenticationForm(request, data = request.POST)

        if loginForm.is_valid():
            usuario = loginForm.cleaned_data.get("username")
            contra = loginForm.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)
                avatar = setAvatar(request)
                return render(request, "AppCoder/inicio.html", {"mensaje" : f"Bienvenido {usuario}", "url" : avatar})

            else:
                return render(request, "AppCoder/inicio.html", {"mensaje" : "Datos incorrectos", "url" : avatar})

        else:
            return render(request, "AppCoder/inicio.html", {"mensaje" : "Formulario erróneo", "url" : avatar})

    loginForm = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"loginForm" : loginForm, "url" : avatar})

def register(request):

    if request.method == "POST":
        
        regForm = UserRegisterForm(request.POST)

        if regForm.is_valid():
            
            username = regForm.cleaned_data['username']
            regForm.save()
            
            return render(request, "AppCoder/inicio.html", {"mensaje" : f"Usuario {username} creado exitosamente"})
        
    else:
            regForm = UserRegisterForm()
    
    return render(request, "AppCoder/register.html" , {"regForm" : regForm})

@login_required
def edit_user(request):
    avatar = setAvatar(request)

    usuario = request.user

    if request.method == "POST":

        editUserForm = UserEditForm(request.POST)

        if editUserForm.is_valid():

            informacion = editUserForm.cleaned_data
        
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "AppCoder/inicio.html", {"mensaje" : f"Usuario {usuario} modificado exitosamente", "url" : avatar})
        
    else:

        editUserForm = UserEditForm(initial= {'email' : usuario.email})
    
    return render(request, "AppCoder/edit_user.html", {"editUserForm" : editUserForm, "usuario" : usuario, "url" : avatar})

@login_required
def avatar_add(request):
    avatar = setAvatar(request)

    if request.method == "POST":

        avatarForm = AvatarForm(request.POST, request.FILES)

        if avatarForm.is_valid():

            u = User.objects.get(username = request.user)
            avatar = Avatar (user = u, imagen = avatarForm.cleaned_data['imagen'])

            avatar.save()

            return render(request, "AppCoder/inicio.html", {"url" : avatar})
    
    else:

        avatarForm = AvatarForm()
    
    return render(request, "AppCoder/avatar_add.html", {"avatarForm" : avatarForm, "url" : avatar})

