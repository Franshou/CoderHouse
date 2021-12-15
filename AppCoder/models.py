from django.db import models
from django.db.models.base import Model

# Create your models here.
class Alumno(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    matricula = models.IntegerField()

    def __str__(self):
        return (f"{self.matricula} - {self.nombre} {self.apellido}")


class Docente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    catedra = models.CharField(max_length=40)

    def __str__(self):
        return (f"{self.catedra} - {self.nombre} {self.apellido}")


class Curso(models.Model):

    comision = models.IntegerField()
    materia = models.CharField(max_length=40)
    
    def __str__(self):
        return (f"{self.comision} - {self.materia}")