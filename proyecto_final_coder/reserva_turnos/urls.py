from django.urls import path

from .views import (
    home_view, 
    list_view, 
    detail_view, 
    search_view, 
    search_with_form_view,
    create_with_form_view,
    )


urlpatterns = [
    path("", home_view, name="reserva_turnos-home"),
    path("list/", list_view, name="reserva_turnos-list"),
    path("detail/<turno_id>", detail_view),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="buscar_turnos"),
    path("crear-con-formulario/", create_with_form_view, name="crear_turnos"),
]