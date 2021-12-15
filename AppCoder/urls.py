from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('alumnos', views.alumnos, name = "Alumnos"),
    path('docentes', views.docentes, name = "Docentes"),
    path('cursos', views.cursos, name = "Cursos"),
    
    path('abmAlumnos', views.abmAlumnos, name = "ABM-Alumnos"),
    path('abmDocentes', views.abmDocentes, name = "ABM-Docentes"),
    path('abmCursos', views.abmCursos, name = "ABM-Cursos"),

]
