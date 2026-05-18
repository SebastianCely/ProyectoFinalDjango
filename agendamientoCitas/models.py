from django.db import models
from django.core.validators import RegexValidator

class TipoCita(models.Model):
    nombre = models.CharField(max_length=200)

class Doctor(models.Model):
    primer_apellido = models.CharField(max_length=15)
    segundo_apellido = models.CharField(max_length=15, null=True, blank=True)
    primer_nombre = models.CharField(max_length=15)
    segundo_nombre = models.CharField(max_length=15, null=True, blank=True)


class Paciente(models.Model):
    primer_apellido = models.CharField(max_length=15)
    segundo_apellido = models.CharField(max_length=15, null=True, blank=True)
    primer_nombre = models.CharField(max_length=15)
    segundo_nombre = models.CharField(max_length=15, null=True, blank=True)
    numero_identificacion = models.PositiveIntegerField(unique=True)
    telefono = models.CharField(max_length=15, default="3159895563", validators=[RegexValidator(regex=r'^\+?\d{7,15}$')])
    email = models.EmailField(max_length=100, default="prueba@hotmail.com")
    direccion = models.CharField(max_length=200, default="calle 66")


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_cita = models.ForeignKey(TipoCita, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()

    class Meta:
        unique_together = ('paciente', 'tipo_cita')
