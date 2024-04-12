from django.shortcuts import render,redirect
from .forms import TurnoSearchForm, TurnoCreateForm
from .models import Turnos

def home_view(request):
    return render(request, "reserva_turnos/home.html")


def list_view(request):
    turnos = Turnos.objects.all()
    contexto_dict = {"todos_los_turnos": turnos}
    return render(request, "reserva_turnos/list.html", contexto_dict)


def detail_view(request, turno_id):
    turno = Turnos.objects.get(id=turno_id)
    contexto_dict = {"turno": turno}
    return render(request, "reserva_turnos/detail.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"turnos": turnos_del_usuario}
    return render(request, "reserva_turnos/list.html", contexto_dict)


def search_with_form_view(request):
    if request.method == "GET":
        form = TurnoSearchForm()
        return render(request, "reserva_turnos/form-search.html", context={"search_form":form})
    elif request.method == "POST":
        form = TurnoSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
        turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        contexto_dict = {"todos_los_turnos": turnos_del_usuario}
        return render(request, "reserva_turnos/list.html", contexto_dict)
    

def create_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_form": TurnoCreateForm()}
        return render(request, "reserva_turnos/form-create.html", contexto)
    elif request.method == "POST":
        form = TurnoCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
            consultorio = form.cleaned_data['consultorio']
            profesional = form.cleaned_data['profesional']
            fecha = form.cleaned_data['fecha']
            hora_inicio = form.cleaned_data['hora_inicio']
            descripcion = form.cleaned_data['descripcion']
            nuevo_turno = Turnos(nombre_de_usuario=nombre_de_usuario,
                                 consultorio=consultorio,
                                 profesional=profesional,
                                 fecha=fecha,
                                 hora_inicio=hora_inicio,
                                 descripcion=descripcion)
            nuevo_turno.save()
            return detail_view(request, nuevo_turno.id)

        # turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        # contexto_dict = {"todos_los_turnos": turnos_del_usuario}
        # return render(request, "reserva_turnos/list.html", contexto_dict)    


def delete_view(request, turno_id):
    turno_a_borrar = Turnos.objects.filter(id=turno_id).first()
    turno_a_borrar.delete()
    return redirect("reserva_turnos-list")


def update_view(request, turno_id):
    turno_a_editar = Turnos.objects.filter(id=turno_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre_de_usuario": turno_a_editar.nombre_de_usuario,
            "consultorio": turno_a_editar.consultorio,
            "profesional": turno_a_editar.profesional,
            "fecha": turno_a_editar.fecha,
            "hora_inicio": turno_a_editar.hora_inicio,
            "descripcion": turno_a_editar.descripcion
        }
        formulario = TurnoCreateForm(initial=valores_iniciales)
        contexto = {
            "update_form": formulario,
            "turno": turno_a_editar
        }
        return render(request, "reserva_turnos/form-update.html", contexto)
    elif request.method == "POST":
        form = TurnoCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
            consultorio = form.cleaned_data['consultorio']
            profesional = form.cleaned_data['profesional']
            fecha = form.cleaned_data['fecha']
            hora_inicio = form.cleaned_data['hora_inicio']
            descripcion = form.cleaned_data['descripcion']
            turno_a_editar.nombre_de_usuario = nombre_de_usuario
            turno_a_editar.consultorio = consultorio
            turno_a_editar.profesional = profesional
            turno_a_editar.fecha = fecha
            turno_a_editar.hora_inicio = hora_inicio
            turno_a_editar.descripcion = descripcion
            turno_a_editar.save()
            return redirect("turno-detail", turno_a_editar.id)


# Vistas basadas en clases "VBC"

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

class TurnosListView(ListView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_list.html'
    context_object_name = 'turnos'


class TurnosDetailView(DetailView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_detail.html'
    context_object_name = 'turnos'


class TurnosCreateView(CreateView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_create.html'
    fields = ['nombre_de_usuario', 'consultorio', 'profesional', 'fecha', 'hora_inicio', 'descripcion']
    success_url = reverse_lazy('vbc_turnos_list')


class TurnosUpdateView(UpdateView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_create.html'
    fields = ['nombre_de_usuario', 'consultorio', 'profesional', 'fecha', 'hora_inicio', 'descripcion']
    context_object_name = 'turno'
    success_url = reverse_lazy('vbc_turnos_list')


class TurnosDeleteView(DeleteView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_confirm_delete.html'
    success_url = reverse_lazy('vbc_turnos_list')


class TurnosSearchView(FormView):
    pass
