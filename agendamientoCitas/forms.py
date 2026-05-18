from django import forms
from . models import Doctor
from . models import Paciente
from . models import Cita

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'primer_apellido',
            'segundo_apellido',
            'primer_nombre',
            'segundo_nombre',
        ]

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'primer_apellido',
            'segundo_apellido',
            'primer_nombre',
            'segundo_nombre',
            'numero_identificacion',
            'telefono',
            'email',
            'direccion',
        ]

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'paciente',
            'tipo_cita',
            'doctor',
            'fecha',
        ]

