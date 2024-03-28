from django.shortcuts import render
from django.http import HttpResponse
from .models import Turnos

def home_view(request):
    return render(request, "reserva_turnos/home.html")

def list_view(request):
    turnos = Turnos.objects.all()
    contexto_dict = {"turnos": turnos}
    return render(request, "reserva_turnos/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"turnos": turnos_del_usuario}
    return render(request, "reserva_turnos/list.html", contexto_dict)


def create_view(request, nombre_de_usuario, consultorio, profesional):
    registro_turnos = Turnos.objects.create(nombre_de_usuario=nombre_de_usuario, consultorio=consultorio, profesional=profesional)
    return HttpResponse(f"Operacion éxitosa. {registro_turnos}")
