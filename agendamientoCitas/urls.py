from django.urls import path, re_path
#from agendamientoCitas import views
from . import views

urlpatterns = [
    path('', views.render_index_view, name='index'),
    path('registrar_doctor/', views.render_registrar_doctor, name='registrardoctor'),
    path('registrar_paciente/', views.render_registrar_paciente, name='registrarpaciente'),
    path('editar_paciente/<id>/', views.render_editar_paciente, name='editarpaciente')
]