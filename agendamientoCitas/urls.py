from django.urls import path, re_path
#from agendamientoCitas import views
from .views import ListarCitasView
from . import views


urlpatterns = [
    path('', views.render_index_view, name='index'),
    path('registrar_doctor/', views.render_registrar_doctor, name='registrardoctor'),
    path('registrar_paciente/', views.render_registrar_paciente, name='registrarpaciente'),
    path('editar_paciente/<id>/', views.render_editar_paciente, name='editarpaciente'),
    path('registrar_cita/', views.render_registrar_cita, name='registrarcita'),
    #path('listado_citas/', views.render_listar_citas, name='listarcitas'),
    path('listado_citas/', ListarCitasView.as_view(), name='listado_citas'),
    path('editar_cita/<id>/', views.render_editar_cita, name='editarcita'),
    path('eliminar_cita/<id>/', views.eliminar_cita, name='eliminarcita'),
]