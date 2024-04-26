from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Consultorio, Profesional, Turnos, Avatar


class TurnoSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")


class ProfesionalSearchForm(forms.Form):
    especialidad = forms.ChoiceField(choices=Profesional.Especialidades.choices, label="Seleccione la especialidad requerida")
    disponible = forms.BooleanField(required=False, label="Sólo profesionales disponibles")


class TurnoCreateForm(forms.ModelForm):
    nombre_de_usuario = forms.CharField(max_length=100)
    class Meta:
        model = Turnos
        fields = ['consultorio', 
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
    def __init__(self, *args, **kwargs):
        super(TurnoCreateForm, self).__init__(*args, **kwargs)
        self.fields = {k: self.fields[k] for k in ['nombre_de_usuario',
                                                   'consultorio',
                                                   'profesional',
                                                   'fecha',
                                                   'hora_inicio',
                                                   'descripcion']} 


class ProfesionalCreateForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre',
                  'disponible',
                  'especialidad', 
                  'descripcion']
        widgets = {
            'nombre': forms.Textarea(attrs={'rows': 1,'placeholder': 'Nombre de profesional'}),
            'especialidad' : forms.Textarea(attrs={'rows': 1,'placeholder': 'Especialidad'}),
            'descripcion' : forms.Textarea(attrs={'rows': 1,'placeholder': 'Descripcion'}),
        }
        labels = {
            'nombre': 'Nombre',
            'disponible': 'Disponible',
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


class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']        