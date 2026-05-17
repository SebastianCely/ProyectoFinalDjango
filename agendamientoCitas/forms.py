from django import forms
from . models import Doctor

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