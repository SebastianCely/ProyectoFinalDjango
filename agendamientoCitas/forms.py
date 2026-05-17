from django import forms
from . models import Doctor
from . models import Paciente

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'primer_apellido',
            'segundo_apellido',
            'primer_nombre',
            'segundo_nombre',
            'tipos_cita',
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