from django import forms
from .models import Consultorio, Profesional, Turnos


class TurnoSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")

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

