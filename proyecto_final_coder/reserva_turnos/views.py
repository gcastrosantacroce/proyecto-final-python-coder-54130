from django.shortcuts import render
from django.http import HttpResponse
from .models import Turnos

def home_view(request):
    return render(request, "reserva_turnos/home.html")


def list_view(request):
    turnos = Turnos.objects.all()
    contexto_dict = {"todos_los_turnos": turnos}
    return render(request, "reserva_turnos/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"turnos": turnos_del_usuario}
    return render(request, "reserva_turnos/list.html", contexto_dict)


def detail_view(request, turno_id):
    turno = Turnos.objects.get(id=turno_id)
    contexto_dict = {"turno": turno}
    return render(request, "reserva_turnos/detail.html", contexto_dict)
