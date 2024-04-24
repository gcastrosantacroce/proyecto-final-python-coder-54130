from django import forms
from django.contrib.auth.models import User
from .models import Consultorio, Profesional, Turnos


class TurnoSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")


class ProfesionalSearchForm(forms.Form):
    especialidad = forms.CharField(max_length=50, required=True, label="Ingresar la especialidad requerida")


class TurnoCreateForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['nombre_de_usuario',
                  'consultorio', 
                  'profesional', 
                  'fecha',
                  'hora_inicio', 
                  'descripcion']
        widgets = {
            'nombre_de_usuario': forms.Textarea(attrs={'rows': 1,'placeholder': 'Nombre de usuario'}),
            'fecha' : forms.TimeInput(attrs={'type':'date'}),
            'hora_inicio' : forms.TimeInput(attrs={'type':'time'}),
        }
        labels = {
            'nombre_de_usuario': 'Usuario',
            'disponible': 'Disponible',
            'fecha': 'Fecha del turno',
            'hora_inicio' : 'Horario',
            'descripcion': 'Detalle',
        }


class ProfesionalCreateForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 
                  'especialidad', 
                  'descripcion']
        widgets = {
            'nombre': forms.Textarea(attrs={'rows': 1,'placeholder': 'Nombre de profesional'}),
            'especialidad' : forms.Textarea(attrs={'rows': 1,'placeholder': 'Especialidad'}),
            'descripcion' : forms.Textarea(attrs={'rows': 1,'placeholder': 'Descripcion'}),
        }
        labels = {
            'nombre': 'Nombre',
            'especialidad': 'Especialidad',
            'descripcion': 'Descripcion',
        }


class ConsultorioCreateForm(forms.ModelForm):
    class Meta:
        model = Consultorio
        fields = ['nombre', 
                  'disponible', 
                  'descripcion']
        widgets = {
            'nombre': forms.Textarea(attrs={'rows': 1,'placeholder': 'Numero de consultorio'}),
            'descripcion' : forms.Textarea(attrs={'rows': 1,'placeholder': 'Descripcion'}),
        }
        labels = {
            'nombre': 'Numero',
            'disponible': 'Disponible',
            'descripcion': 'Descripcion',
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']