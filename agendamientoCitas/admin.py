from django.contrib import admin

from .models import Doctor
from .models import TipoCita
from .models import Paciente
from .models import Cita

admin.site.register(Doctor)
admin.site.register(TipoCita)
admin.site.register(Paciente)
admin.site.register(Cita)