from django.shortcuts import render
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
        form = TurnoCreateForm()
        return render(request, "reserva_turnos/form-create.html", context={"create_form":form})
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

        turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        contexto_dict = {"todos_los_turnos": turnos_del_usuario}
        return render(request, "reserva_turnos/list.html", contexto_dict)    



