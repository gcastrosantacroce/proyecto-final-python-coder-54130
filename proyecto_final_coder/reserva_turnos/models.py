from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Consultorio(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {'Disponible' if self.disponible else 'No Disponible'} "
    

class Profesional(models.Model):
    class Especialidades(models.TextChoices):
        CARDIOLOGIA = 'CARDIOLOGIA', 'Cardiología'
        DERMATOLOGIA = 'DERMATOLOGIA', 'Dermatología'
        ENDOCRINOLOGIA = 'ENDOCRINOLOGIA', 'Endocrinología'
        GASTROENTEROLOGIA = 'GASTROENTEROLOGIA', 'Gastroenterología'
        GINECOLOGIA = 'GINECOLOGIA', 'Ginecología'
        HEMATOLOGIA = 'HEMATOLOGIA', 'Hematología'
        HEPATOLOGIA = 'HEPATOLOGIA', 'Hepatología'
        INMUNOLOGIA = 'INMUNOLOGIA', 'Inmunología'
        NEFROLOGIA = 'NEFROLOGIA', 'Nefrología'
        NEUROLOGIA = 'NEUROLOGIA', 'Neurología'
        ONCOLOGIA = 'ONCOLOGIA', 'Oncología'
        OFTALMOLOGIA = 'OFTALMOLOGIA', 'Oftalmología'
        PSICOLOGIA = 'PSICOLOGIA', 'Psicología'
        PSIQUIATRIA = 'PSIQUIATRIA', 'Psiquiatría'
        TRAUMATOLOGIA = 'TRAUMATOLOGIA', 'Traumatología'
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    # especialidad = models.CharField(max_length=20)
    especialidad = models.CharField(
        max_length=17,
        choices=Especialidades.choices,
        default=Especialidades.CARDIOLOGIA,
    )
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {'Disponible' if self.disponible else 'No Disponible'} "


class Turnos(models.Model):
    nombre_de_usuario = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    # nombre_de_usuario = models.CharField(max_length=100)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, related_name='reservas')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, default = True)
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.consultorio.nombre} - {self.fecha}"