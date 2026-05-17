from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . forms import DoctorForm
from . forms import PacienteForm
from .models import TipoCita
from .models import Doctor
from .models import Paciente


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
