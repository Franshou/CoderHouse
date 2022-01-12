from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('alumnos', views.alumnos, name = "Alumnos"),
    path('docentes', views.docentes, name = "Docentes"),
    path('cursos', views.cursos, name = "Cursos"),
    path('about', views.about, name = "About"),
    
    path('abmAlumnos', views.abmAlumnos, name = "ABM-Alumnos"),
    path('abmDocentes', views.abmDocentes, name = "ABM-Docentes"),
    path('abmCursos', views.abmCursos, name = "ABM-Cursos"),

    #login/logout
    path('login', views.login_request, name = "Login"),
    path('register', views.register, name = "Register"),
    path('logout', LogoutView.as_view(template_name = 'AppCoder/logout.html'), name = "Logout"),
    path('edit_user', views.edit_user, name = "EditUser"),
    path('avatar_add', views.avatar_add, name = "AvatarAdd"),

    #views para CBVs
    path('alumnos/list', views.AlumnoList.as_view(), name = "AluList"),
    path(r'^(?P<pk>\a+)$', views.AlumnoDetail.as_view(), name = "AluDetail"),
    path(r'^nuevo$', views.AlumnoCreate.as_view(), name = "AluNew"),
    path(r'^editar/((?P<pk>\a+)$', views.AlumnoUpdate.as_view(), name = "AluEdit"),
    path(r'^borrar/((?P<pk>\a+)$', views.AlumnoDelete.as_view(), name = "AluDelete"),

    path('docentes/list', views.DocenteList.as_view(), name = "DocList"),
    path(r'^(?P<pk>\d+)$', views.DocenteDetail.as_view(), name = "DocDetail"),
    path(r'^nuevo$', views.DocenteCreate.as_view(), name = "DocNew"),
    path(r'^editar/((?P<pk>\d+)$', views.DocenteUpdate.as_view(), name = "DocEdit"),
    path(r'^borrar/((?P<pk>\d+)$', views.DocenteDelete.as_view(), name = "DocDelete"),

    path('cursos/list', views.CursoList.as_view(), name = "CurList"),
    path(r'^(?P<pk>\c+)$', views.CursoDetail.as_view(), name = "CurDetail"),
    path(r'^nuevo$', views.CursoCreate.as_view(), name = "CurNew"),
    path(r'^editar/((?P<pk>\c+)$', views.CursoUpdate.as_view(), name = "CurEdit"),
    path(r'^borrar/((?P<pk>\c+)$', views.CursoDelete.as_view(), name = "CurDelete"),

    
]
