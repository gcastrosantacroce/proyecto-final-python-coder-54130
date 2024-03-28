from django.urls import path

from .views import home_view, list_view, search_view, create_view


urlpatterns = [
    path("", home_view, name="reserva_turnos-home"),
    path("list/", list_view, name="reserva_turnos-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("crear/<nombre_de_usuario>/<consultorio>/<profesional>", create_view),
]