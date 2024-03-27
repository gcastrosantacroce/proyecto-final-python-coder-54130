from django.shortcuts import render
from django.http import HttpResponse
from .models import Registro

def home_view(request):
    return render(request, "application1/home.html")

# def list_view(request):
#     contexto_dict = {
#         'reservas': [
#             {"usuario": "Emiliano Martínez ", "sala": "aruba"},
#             {"usuario": "Nicolas Otamendi ", "sala": "italia"},
#             {"usuario": "Nahuel Molina ", "sala": "multisala"},
#         ]
#     }
#     return render(request, "bookings/list.html", contexto_dict)

# ASI SERIA UN EJEMPLO  CON UN DICCIONARIO

def list_view(request):
    registros = Registro.objects.all()
    contexto_dict = {"registros": registros}
    return render(request, "application1/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    registro_del_usuario = Registro.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"registros": registro_del_usuario}
    return render(request, "application1/list.html", contexto_dict)


def create_view(request, nombre_de_usuario, mail):
    registro = Registro.objects.create(nombre_de_usuario=nombre_de_usuario, mail=mail)
    return HttpResponse(f"Operacion éxitosa. {registro}")


# Create your views here.
