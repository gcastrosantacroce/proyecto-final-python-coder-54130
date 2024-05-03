from django.shortcuts import render,redirect, HttpResponse
from .forms import (
    TurnoCreateForm, 
    TurnoSearchForm, 
    ProfesionalCreateForm, 
    ProfesionalSearchForm, 
    ConsultorioCreateForm, 
    UserEditForm,
    AvatarCreateForm,
    )
from .models import Turnos, Profesional, Consultorio, Avatar

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


# -----------------------------------------------------------------------------
#USER
# -----------------------------------------------------------------------------

def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect('reserva_turnos-home')

    return render(request, 'reserva_turnos/login.html', {'form': form})

def user_logout_view(request):
    logout(request)
    return redirect("login")

def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("reserva_turnos-home")

    return render(request, "reserva_turnos/crear_usuario.html", {"form": form})

def avatar_view(request):
    if request.method == "GET":
        contexto = {"form": AvatarCreateForm()}
    else:
        form = AvatarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user=request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user=request.user)
            nuevo_avatar.save()
            return redirect("reserva_turnos-home")
        else:
            contexto = {"form": form}


    return render(request, "reserva_turnos/avatar_create.html", context=contexto)

@login_required
def home_view(request):
    return render(request, "reserva_turnos/home.html")

# -----------------------------------------------------------------------------
#TURNOS
# -----------------------------------------------------------------------------

@login_required
def list_view(request):
    turnos = Turnos.objects.all()
    contexto_dict = {"todos_los_turnos": turnos}
    return render(request, "reserva_turnos/list.html", contexto_dict)

@login_required
def create_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_form": TurnoCreateForm()}
        return render(request, "reserva_turnos/form-create.html", contexto)
    elif request.method == "POST":
        form = TurnoCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
            if User.objects.filter(username=nombre_de_usuario).exists():
                user = User.objects.get(username=nombre_de_usuario)
            else:
                return HttpResponse('El usuario ingresado no existe')  
            consultorio = form.cleaned_data['consultorio']
            profesional = form.cleaned_data['profesional']
            fecha = form.cleaned_data['fecha']
            hora_inicio = form.cleaned_data['hora_inicio']
            descripcion = form.cleaned_data['descripcion']
            nuevo_turno = Turnos(nombre_de_usuario=user,
                                 consultorio=consultorio,
                                 profesional=profesional,
                                 fecha=fecha,
                                 hora_inicio=hora_inicio,
                                 descripcion=descripcion)
            nuevo_turno.save()
            return detail_view(request, nuevo_turno.id)
        else:
            contexto = {"create_form": TurnoCreateForm()}
            return render(request, "reserva_turnos/form-create.html", contexto)
        # turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        # contexto_dict = {"todos_los_turnos": turnos_del_usuario}
        # return render(request, "reserva_turnos/list.html", contexto_dict)   

@login_required
def search_view(request, nombre_de_usuario):
    turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"turnos": turnos_del_usuario}
    return render(request, "reserva_turnos/list.html", contexto_dict)

@login_required
def search_with_form_view(request):
    if request.method == "GET":
        form = TurnoSearchForm()
        return render(request, "reserva_turnos/form-search.html", context={"search_form":form})
    elif request.method == "POST":
        form = TurnoSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
            if User.objects.filter(username=nombre_de_usuario).exists():
                user = User.objects.get(username=nombre_de_usuario)
            else:
                return HttpResponse('El usuario ingresado no existe') 
            turnos_del_usuario = Turnos.objects.filter(nombre_de_usuario=user).all()
            contexto_dict = {"todos_los_turnos": turnos_del_usuario}
            return render(request, "reserva_turnos/list.html", contexto_dict)

@login_required
def detail_view(request, turno_id):
    turno = Turnos.objects.get(id=turno_id)
    contexto_dict = {"turno": turno}
    return render(request, "reserva_turnos/detail.html", contexto_dict)

@login_required
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
            if User.objects.filter(username=nombre_de_usuario).exists():
                user = User.objects.get(username=nombre_de_usuario)
            consultorio = form.cleaned_data['consultorio']
            profesional = form.cleaned_data['profesional']
            fecha = form.cleaned_data['fecha']
            hora_inicio = form.cleaned_data['hora_inicio']
            descripcion = form.cleaned_data['descripcion']
            turno_a_editar.nombre_de_usuario = user
            turno_a_editar.consultorio = consultorio
            turno_a_editar.profesional = profesional
            turno_a_editar.fecha = fecha
            turno_a_editar.hora_inicio = hora_inicio
            turno_a_editar.descripcion = descripcion
            turno_a_editar.save()
            return redirect("turno-detail", turno_a_editar.id)

@login_required
def delete_view(request, turno_id):
    turno_a_borrar = Turnos.objects.filter(id=turno_id).first()
    turno_a_borrar.delete()
    return redirect("reserva_turnos-list")

# -----------------------------------------------------------------------------
#PROFESIONALES
# -----------------------------------------------------------------------------

@login_required
def list_profesional_view(request):
    profesionales = Profesional.objects.all()
    contexto_dict = {"todos_los_profesionales": profesionales}
    return render(request, "reserva_turnos/list_profesional.html", contexto_dict)

@login_required
def create_profesional_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_profesional_form": ProfesionalCreateForm()}
        return render(request, "reserva_turnos/form-create_profesional.html", contexto)
    elif request.method == "POST":
        form = ProfesionalCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            especialidad = form.cleaned_data['especialidad']
            descripcion = form.cleaned_data['descripcion']
            nuevo_profesional = Profesional(nombre=nombre,
                                 especialidad=especialidad,
                                 descripcion=descripcion)
            nuevo_profesional.save()
            return detail_profesional_view(request, nuevo_profesional.id)

@login_required
def search_profesional_with_form_view(request):
    if request.method == "GET":
        form = ProfesionalSearchForm()
        return render(request, "reserva_turnos/form-search_profesional.html", context={"search_profesional_form":form})
    elif request.method == "POST":
        form = ProfesionalSearchForm(request.POST)
        if form.is_valid():
            descartar_no_disponibles = form.cleaned_data["disponible"]
            especialidad = form.cleaned_data['especialidad']

            profesionales_encontrados = Profesional.objects.filter(especialidad=especialidad)

            if descartar_no_disponibles:
                profesionales_encontrados = profesionales_encontrados.filter( disponible=True)

            if especialidad:
                profesionales_encontrados = profesionales_encontrados.filter(especialidad=especialidad)

        contexto_dict = {"todos_los_profesionales": profesionales_encontrados}
        return render(request, "reserva_turnos/list_profesional.html", contexto_dict)  
    
    else:
            return render(request,"reserva_turnos/form-search_profesional.html",context={"search_profesional_form":form})
    
@login_required
def detail_profesional_view(request, profesional_id):
    profesional = Profesional.objects.get(id=profesional_id)
    contexto_dict = {"profesional": profesional}
    return render(request, "reserva_turnos/detail_profesional.html", contexto_dict)

@login_required
def update_profesional_view(request, profesional_id):
    profesional_a_editar = Profesional.objects.filter(id=profesional_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": profesional_a_editar.nombre,
            "disponible": profesional_a_editar.disponible,
            "especialidad": profesional_a_editar.especialidad,
            "descripcion": profesional_a_editar.descripcion,
        }
        formulario = ProfesionalCreateForm(initial=valores_iniciales)
        contexto = {
            "update_profesional_form": formulario,
            "profesional": profesional_a_editar
        }
        return render(request, "reserva_turnos/form-update_profesional.html", contexto)
    elif request.method == "POST":
        form = ProfesionalCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            especialidad = form.cleaned_data['especialidad']
            descripcion = form.cleaned_data['descripcion']
            profesional_a_editar.nombre = nombre
            profesional_a_editar.disponible = disponible
            profesional_a_editar.especialidad = especialidad
            profesional_a_editar.descripcion = descripcion
            profesional_a_editar.save()
            return redirect("profesional-detail", profesional_a_editar.id)

@login_required
def delete_profesional_view(request, profesional_id):
    profesional_a_borrar = Profesional.objects.filter(id=profesional_id).first()
    profesional_a_borrar.delete()
    return redirect("profesionales-list")

# -----------------------------------------------------------------------------
#CONSULTORIOS
# -----------------------------------------------------------------------------

@login_required
def list_consultorio_view(request):
    consultorios = Consultorio.objects.all()
    contexto_dict = {"todos_los_consultorios": consultorios}
    return render(request, "reserva_turnos/list_consultorio.html", contexto_dict)

@login_required
def create_consultorio_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_consultorio_form": ConsultorioCreateForm()}
        return render(request, "reserva_turnos/form-create_consultorio.html", contexto)
    elif request.method == "POST":
        form = ConsultorioCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            descripcion = form.cleaned_data['descripcion']
            nuevo_consultorio = Consultorio(nombre=nombre,
                                 disponible=disponible,
                                 descripcion=descripcion)
            nuevo_consultorio.save()
            return detail_consultorio_view(request, nuevo_consultorio.id)

@login_required
def detail_consultorio_view(request, consultorio_id):
    consultorio = Consultorio.objects.get(id=consultorio_id)
    contexto_dict = {"consultorio": consultorio}
    return render(request, "reserva_turnos/detail_consultorio.html", contexto_dict)

@login_required
def update_consultorio_view(request, consultorio_id):
    consultorio_a_editar = Consultorio.objects.filter(id=consultorio_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": consultorio_a_editar.nombre,
            "disponible": consultorio_a_editar.disponible,
            "descripcion": consultorio_a_editar.descripcion,
        }
        formulario = ConsultorioCreateForm(initial=valores_iniciales)
        contexto = {
            "update_consultorio_form": formulario,
            "consultorio": consultorio_a_editar
        }
        return render(request, "reserva_turnos/form-update_consultorio.html", contexto)
    elif request.method == "POST":
        form = ConsultorioCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            descripcion = form.cleaned_data['descripcion']
            consultorio_a_editar.nombre = nombre
            consultorio_a_editar.disponible = disponible
            consultorio_a_editar.descripcion = descripcion
            consultorio_a_editar.save()
            return redirect("consultorio-detail", consultorio_a_editar.id)        

@login_required
def delete_consultorio_view(request, consultorio_id):
    consultorio_a_borrar = Consultorio.objects.filter(id=consultorio_id).first()
    consultorio_a_borrar.delete()
    return redirect("consultorios-list")


# -----------------------------------------------------------------------------
# VISTAS BASADAS EN CLASES "VBC"
# -----------------------------------------------------------------------------


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# -----------------------------------------------------------------------------
#USER
# -----------------------------------------------------------------------------

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'reserva_turnos/user_edit.html'
    success_url = reverse_lazy('reserva_turnos-home')

    def get_object(self):
        return self.request.user

# -----------------------------------------------------------------------------
#TURNOS
# -----------------------------------------------------------------------------

class TurnosListView(LoginRequiredMixin,ListView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_list.html'
    context_object_name = 'turnos'


class TurnosDetailView(LoginRequiredMixin,DetailView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_detail.html'
    context_object_name = 'turnos'


class TurnosCreateView(LoginRequiredMixin,CreateView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_create.html'
    fields = ['nombre_de_usuario', 'consultorio', 'profesional', 'fecha', 'hora_inicio', 'descripcion']
    success_url = reverse_lazy('vbc_turnos_list')


class TurnosUpdateView(LoginRequiredMixin,UpdateView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_create.html'
    fields = ['nombre_de_usuario', 'consultorio', 'profesional', 'fecha', 'hora_inicio', 'descripcion']
    context_object_name = 'turno'
    success_url = reverse_lazy('vbc_turnos_list')


class TurnosDeleteView(LoginRequiredMixin,DeleteView):
    model = Turnos
    template_name = 'reserva_turnos/vbc/turnos_confirm_delete.html'
    success_url = reverse_lazy('vbc_turnos_list')


class TurnosSearchView(LoginRequiredMixin,FormView):
    pass

# -----------------------------------------------------------------------------
#PROFESIONALES
# -----------------------------------------------------------------------------

class ProfesionalesListView(LoginRequiredMixin,ListView):
    model = Profesional
    template_name = 'reserva_turnos/vbc/profesional_list.html'
    context_object_name = 'profesionales'


class ProfesionalesDetailView(LoginRequiredMixin,DetailView):
    model = Profesional
    template_name = 'reserva_turnos/vbc/profesional_detail.html'
    context_object_name = 'profesionales'  


class ProfesionalesCreateView(LoginRequiredMixin,CreateView):
    model = Profesional
    template_name = 'reserva_turnos/vbc/profesional_create.html'
    fields = ['nombre','disponible','especialidad','descripcion']
    success_url = reverse_lazy('vbc_profesionales_list')


class ProfesionalesUpdateView(LoginRequiredMixin,UpdateView):
    model = Profesional
    template_name = 'reserva_turnos/vbc/profesional_create.html'
    fields = ['nombre','disponible','especialidad','descripcion']
    context_object_name = 'profesionales'
    success_url = reverse_lazy('vbc_profesionales_list')          


class ProfesionalesDeleteView(LoginRequiredMixin,DeleteView):
    model = Profesional
    template_name = 'reserva_turnos/vbc/profesional_confirm_delete.html'
    success_url = reverse_lazy('vbc_profesionales_list')      

# -----------------------------------------------------------------------------
#CONSULTORIOS
# -----------------------------------------------------------------------------

class ConsultoriosListView(LoginRequiredMixin,ListView):
    model = Consultorio
    template_name = 'reserva_turnos/vbc/consultorio_list.html'
    context_object_name = 'consultorios'


class ConsultoriosDetailView(LoginRequiredMixin,DetailView):
    model = Consultorio
    template_name = 'reserva_turnos/vbc/consultorio_detail.html'
    context_object_name = 'consultorios'    


class ConsultoriosCreateView(LoginRequiredMixin,CreateView):
    model = Consultorio
    template_name = 'reserva_turnos/vbc/consultorio_create.html'
    fields = ['nombre', 'disponible','descripcion']
    success_url = reverse_lazy('vbc_consultorios_list')


class ConsultoriosUpdateView(LoginRequiredMixin,UpdateView):
    model = Consultorio
    template_name = 'reserva_turnos/vbc/consultorio_create.html'
    fields = ['nombre', 'disponible','descripcion']
    context_object_name = 'consultorios'
    success_url = reverse_lazy('vbc_consultorios_list')      


class ConsultoriosDeleteView(LoginRequiredMixin,DeleteView):
    model = Consultorio
    template_name = 'reserva_turnos/vbc/consultorio_confirm_delete.html'
    success_url = reverse_lazy('vbc_consultorios_list')              