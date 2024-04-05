from django.urls import path

from .views import home_view, list_view, search_view, detail_view


urlpatterns = [
    path("", home_view, name="reserva_turnos-home"),
    path("detail/<turno_id>", detail_view),
    path("list/", list_view, name="reserva_turnos-list"),
    path("buscar/<nombre_de_usuario>", search_view),
]