from django import forms

class AlumnosForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    matricula = forms.IntegerField(required=True)

class DocentesForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    catedra = forms.CharField(required=True)

class CursosForm(forms.Form):
    comision = forms.IntegerField(required=True)
    materia = forms.CharField(required=True)