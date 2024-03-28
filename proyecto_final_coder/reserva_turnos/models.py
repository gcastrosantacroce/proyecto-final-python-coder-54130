from django.db import models

class Turnos(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    consultorio = models.CharField(max_length=50)
    profesional = models.CharField(max_length=50)

    def __str__(self):
        return f"Ha registrado un turno para el usuario {self.nombre_de_usuario} en el consultorio {self.consultorio} con el profesional {self.profesional}"
