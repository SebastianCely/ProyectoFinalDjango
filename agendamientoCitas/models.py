from django.db import models

class TipoCita(models.Model):
    nombre = models.CharField(max_length=200)

class Doctor(models.Model):
    primer_apellido = models.CharField(max_length=15)
    segundo_apellido = models.CharField(max_length=15, null=True)
    primer_nombre = models.CharField(max_length=15)
    segundo_nombre = models.CharField(max_length=15, null=True)
    tipos_cita = models.ManyToManyField(TipoCita, related_name='doctores')


class Paciente(models.Model):
    primer_apellido = models.CharField(max_length=15)
    segundo_apellido = models.CharField(max_length=15, null=True)
    primer_nombre = models.CharField(max_length=15)
    segundo_nombre = models.CharField(max_length=15, null=True)
    numero_identificacion = models.PositiveIntegerField()


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_cita = models.ForeignKey(TipoCita, on_delete=models.CASCADE)
    fecha = models.DateField()
