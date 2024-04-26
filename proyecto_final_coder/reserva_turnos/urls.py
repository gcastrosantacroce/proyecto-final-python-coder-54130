from django.urls import path

from .views import (
    # USER
    home_view,
    user_creation_view,
    UserUpdateView,
    user_login_view,
    user_logout_view,
    avatar_view,
    # TURNOS
    list_view,
    TurnosListView, 
    detail_view,
    TurnosDetailView, 
    search_view,
    search_with_form_view,
    TurnosSearchView, 
    create_with_form_view,
    TurnosCreateView,
    delete_view,
    TurnosDeleteView,
    update_view,
    TurnosUpdateView,
    # PROFESIONAL
    list_profesional_view,
    ProfesionalesListView,
    create_profesional_with_form_view,
    ProfesionalesCreateView,
    detail_profesional_view,
    ProfesionalesDetailView,
    delete_profesional_view,
    ProfesionalesDeleteView,
    update_profesional_view,
    ProfesionalesUpdateView,
    # CONSULTORIOS
    list_consultorio_view,
    ConsultoriosListView,
    create_consultorio_with_form_view,
    ConsultoriosCreateView,
    search_profesional_with_form_view,
    detail_consultorio_view,
    ConsultoriosDetailView,
    delete_consultorio_view,
    ConsultoriosDeleteView,
    update_consultorio_view,
    ConsultoriosUpdateView,
    )


urlpatterns = [
    #USER 
    path("", home_view, name="reserva_turnos-home"),
    path('crear-usuario/', user_creation_view, name='crear-usuario'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('avatar/add/', avatar_view, name='avatar_add'),
    #TURNOS 
    path("list/", list_view, name="reserva_turnos-list"),
    path("detail/<turno_id>", detail_view, name = "turno-detail"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="buscar_turnos"),
    path("crear-con-formulario/", create_with_form_view, name="crear_turnos"),
    path("delete/<turno_id>", delete_view, name="turno-delete"),
    path("update/<turno_id>", update_view, name="turno-update"),
    #PROFESIONALES 
    path("crear-profesional-con-formulario/", create_profesional_with_form_view, name="crear_profesional"),
    path("profesionales-list/", list_profesional_view, name="profesionales-list"),
    path("profesional-detail/<profesional_id>", detail_profesional_view, name = "profesional-detail"),
    path("profesional-delete/<profesional_id>", delete_profesional_view, name="profesional-delete"),
    path("profesional-update/<profesional_id>", update_profesional_view, name="profesional-update"),
    path("buscar-profesional-con-formulario/", search_profesional_with_form_view, name="buscar_profesional"),
    #CONSULTORIOS
    path("crear-consultorio-con-formulario/", create_consultorio_with_form_view, name="crear_consultorio"),
    path("consultorios-list/", list_consultorio_view, name="consultorios-list"),
    path("consultorio-detail/<consultorio_id>", detail_consultorio_view, name = "consultorio-detail"),
    path("consultorio-delete/<consultorio_id>", delete_consultorio_view, name="consultorio-delete"),
    path("consultorio-update/<consultorio_id>", update_consultorio_view, name="consultorio-update"), 


    #Vistas basadas en clases "VBC"
    #USER 
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    #TURNOS 
    path("vbc/turnos/list", TurnosListView.as_view(), name="vbc_turnos_list"),
    path("vbc/turnos/create/", TurnosCreateView.as_view(), name='vbc_turnos_create'),
    path("vbc/turnos/search/", TurnosSearchView.as_view(), name='vbc_turnos_search'),
    path("vbc/turnos/<int:pk>/detail", TurnosDetailView.as_view(), name='vbc_turnos_detail'),
    path("vbc/turnos/<int:pk>/update/", TurnosUpdateView.as_view(), name='vbc_turnos_update'),
    path("vbc/turnos/<int:pk>/delete/", TurnosDeleteView.as_view(), name='vbc_turnos_delete'),
    #PROFESIONALES 
    path("vbc/profesionales/list", ProfesionalesListView.as_view(), name="vbc_profesionales_list"),
    path("vbc/profesionales/create/", ProfesionalesCreateView.as_view(), name='vbc_profesionales_create'),
    path("vbc/profesionales/<int:pk>/detail", ProfesionalesDetailView.as_view(), name="vbc_profesionales_detail"),
    path("vbc/profesionales/<int:pk>/update/", ProfesionalesUpdateView.as_view(), name='vbc_profesionales_update'),
    path("vbc/profesionales/<int:pk>/delete/", ProfesionalesDeleteView.as_view(), name='vbc_profesionales_delete'),
    #CONSULTORIOS
    path("vbc/consultorios/list", ConsultoriosListView.as_view(), name="vbc_consultorios_list"),
    path("vbc/consultorios/create/", ConsultoriosCreateView.as_view(), name='vbc_consultorios_create'),
    path("vbc/consultorios/<int:pk>/detail", ConsultoriosDetailView.as_view(), name="vbc_consultorios_detail"),
    path("vbc/consultorios/<int:pk>/update/", ConsultoriosUpdateView.as_view(), name='vbc_consultorios_update'),
    path("vbc/consultorios/<int:pk>/delete/", ConsultoriosDeleteView.as_view(), name='vbc_consultorios_delete'),
]