from django.contrib import admin

from .models import Turnos, Consultorio, Profesional

admin.site.register(Turnos)
admin.site.register(Consultorio)
admin.site.register(Profesional)
