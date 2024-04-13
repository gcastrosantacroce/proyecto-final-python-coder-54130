from django.urls import path

from .views import (
    home_view, 
    list_view, 
    detail_view, 
    search_view, 
    search_with_form_view,
    create_with_form_view,
    delete_view,
    update_view,
    # VBC
    TurnosListView,
    TurnosDetailView,
    TurnosDeleteView,
    TurnosUpdateView,
    TurnosCreateView,
    TurnosSearchView,
    ProfesionalesListView,
    ProfesionalesDetailView,
    ProfesionalesCreateView,
    ProfesionalesUpdateView,
    ProfesionalesDeleteView,
    ConsultoriosListView,
    ConsultoriosDetailView,
    ConsultoriosCreateView,
    ConsultoriosUpdateView,
    ConsultoriosDeleteView,
    )


urlpatterns = [
    path("", home_view, name="reserva_turnos-home"),
    path("list/", list_view, name="reserva_turnos-list"),
    path("detail/<turno_id>", detail_view, name = "turno-detail"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="buscar_turnos"),
    path("crear-con-formulario/", create_with_form_view, name="crear_turnos"),
    path("delete/<turno_id>", delete_view, name="turno-delete"),
    path("update/<turno_id>", update_view, name="turno-update"),
    #Vistas basadas en clases "VBC"
    path("vbc/turnos/list", TurnosListView.as_view(), name="vbc_turnos_list"),
    path("vbc/turnos/create/", TurnosCreateView.as_view(), name='vbc_turnos_create'),
    path("vbc/turnos/search/", TurnosSearchView.as_view(), name='vbc_turnos_search'),
    path("vbc/turnos/<int:pk>/detail", TurnosDetailView.as_view(), name='vbc_turnos_detail'),
    path("vbc/turnos/<int:pk>/update/", TurnosUpdateView.as_view(), name='vbc_turnos_update'),
    path("vbc/turnos/<int:pk>/delete/", TurnosDeleteView.as_view(), name='vbc_turnos_delete'),
    path("vbc/profesionales/list", ProfesionalesListView.as_view(), name="vbc_profesionales_list"),
    path("vbc/profesionales/create/", ProfesionalesCreateView.as_view(), name='vbc_profesionales_create'),
    path("vbc/profesionales/<int:pk>/detail", ProfesionalesDetailView.as_view(), name="vbc_profesionales_detail"),
    path("vbc/profesionales/<int:pk>/update/", ProfesionalesUpdateView.as_view(), name='vbc_profesionales_update'),
    path("vbc/profesionales/<int:pk>/delete/", ProfesionalesDeleteView.as_view(), name='vbc_profesionales_delete'),
    path("vbc/consultorios/list", ConsultoriosListView.as_view(), name="vbc_consultorios_list"),
    path("vbc/consultorios/create/", ConsultoriosCreateView.as_view(), name='vbc_consultorios_create'),
    path("vbc/consultorios/<int:pk>/detail", ConsultoriosDetailView.as_view(), name="vbc_consultorios_detail"),
    path("vbc/consultorios/<int:pk>/update/", ConsultoriosUpdateView.as_view(), name='vbc_consultorios_update'),
    path("vbc/consultorios/<int:pk>/delete/", ConsultoriosDeleteView.as_view(), name='vbc_consultorios_delete'),

]