from django.shortcuts import render
from django.views import generic
from . forms import DoctorForm
from .models import TipoCita


def render_index_view(request):
    return render(request, 'index.html')

def render_registrar_doctor(request):
    tipos_cita = TipoCita.objects.all()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = DoctorForm()
    return render(request, 'registrar_doctor.html', {'form':form, 'tipos_cita': tipos_cita})
