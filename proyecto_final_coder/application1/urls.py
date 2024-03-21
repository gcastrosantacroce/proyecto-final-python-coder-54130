from django.urls import path

from django.http import HttpResponse


def mi_vista(xx):
    return HttpResponse("<h3>Bienvenidos a la aplicación de Reservas</h3>")


urlpatterns = [
    path("", mi_vista),
]