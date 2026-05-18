from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from . forms import DoctorForm
from . forms import PacienteForm
from . forms import CitaForm
from .models import TipoCita
from .models import Doctor
from .models import Paciente
from .models import Cita


def render_index_view(request):
    return render(request, 'index.html')

def render_registrar_doctor(request):
    tipos_cita = TipoCita.objects.all()
    doctores = Doctor.objects.all()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/citas/registrar_doctor')

    else:
        form = DoctorForm()
    return render(request, 'registrar_doctor.html', {'form':form, 'tipos_cita': tipos_cita, 'doctores': doctores})


def render_registrar_paciente(request):
    pacientes = Paciente.objects.all()
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/citas/registrar_paciente')

    else:
        form = PacienteForm()
    return render(request, 'registrar_paciente.html', {'form':form, 'pacientes': pacientes})

def render_editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id = id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('/citas/registrar_paciente')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'editar_info_paciente.html', {'form': form, 'paciente': paciente})


def render_registrar_cita(request):
    paciente = Paciente.objects.all()
    doctor = Doctor.objects.all()
    tipo_cita = TipoCita.objects.all()
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/citas/listado_citas')
    else:
        form = CitaForm()
    return render(request, 'registrar_cita.html', {'form': form, 'paciente': paciente, 'doctor': doctor, 'tipo_cita': tipo_cita})

#def render_listar_citas(request):
    #cita = Cita.objects.all()
    #return render(request, 'listado_citas.html', {'cita': cita})
class ListarCitasView(ListView):
    model = Cita
    template_name = 'listado_citas.html'
    context_object_name = 'cita'

def render_editar_cita(request, id):
    dato = get_object_or_404(Cita, id=id)
    pacientes = Paciente.objects.all()
    tipos_cita = TipoCita.objects.all()
    doctores = Doctor.objects.all()

    if request.method == 'POST':
        form = CitaForm(request.POST, instance=dato,)
        if form.is_valid():
            form.save()
            return redirect('/citas/listado_citas')
    else:
        form = CitaForm(instance=dato)
    return render(request, 'editar_info_cita.html', {'form': form, 'dato' : dato, 'pacientes' : pacientes, 'tipos_cita' : tipos_cita, 'doctores': doctores})

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id = id)
    cita.delete()
    return redirect('/citas/listado_citas')