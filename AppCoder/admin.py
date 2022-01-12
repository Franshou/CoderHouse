from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Avatar)