from django.db import models

# class Registro:
#     def __init__(self, nombre_de_usuario, mail):
#         self.nombre_de_usuario = nombre_de_usuario
#         self.mail = mail
#
#     def __str__(self):
#         return f"Este es el usuario {self.nombre_de_usuario} cuyo mail es {self.mail}"

class Registro(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return f"Ha registrado el usuario {self.nombre_de_usuario} con mail {self.mail}"
    
# Create your models here.
