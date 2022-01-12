from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = "Usuario")
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget=forms.PasswordInput)

    email = forms.EmailField()
    
    first_name = forms.CharField(label = "Nombre")
    last_name = forms.CharField(label = "Apellido")
    
    imagen_avatar = forms.ImageField(label = "Avatar", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'imagen_avatar']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label= "Modificar e-mail")
    password1 = forms.CharField(label = "Modificar contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label = "Repita la contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label = "Modificar nombre", required=False)
    last_name = forms.CharField(label = "Modificar apellido", required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


