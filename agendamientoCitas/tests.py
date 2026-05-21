from django.test import TestCase
from django.urls import reverse
from .models import Cita, Paciente, TipoCita, Doctor

class AgendarCitaTest(TestCase):
    def parametrizarDatos(self):
        self.paciente = Paciente.objects.create(primer_nombre = "Juan", primer_apellido = "Lopez", numero_identificacion = 1000898575, email = "prueba@hotmail.com", direccion = "calle 99")
        self.tipoCita = TipoCita.objects.create(nombre = "General")
        self.doctor = Doctor.objects.create(primer_nombre = "Edison", primer_apellido = "Cavani")
    
    def crear_cita_test(self):
        cita = self.client.post('/citas/registrar_cita', {
            'paciente': self.paciente.id,
            'tipo_cita': self.tipo.id,
            'doctor': self.doctor.id,
            'fecha': '2026-05-25'
        })
        self.assertEqual(cita.status_code, 302)
        self.assertEqual(Cita.objects.count(), 1)



class ListarCitasTest(TestCase):
    def test_listado_responde_200(self):
        response = self.client.get(reverse('listado_citas'))
        self.assertEqual(response.status_code, 200)


