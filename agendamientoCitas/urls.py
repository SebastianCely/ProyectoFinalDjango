from django.urls import path, re_path
#from agendamientoCitas import views
from . import views

urlpatterns = [
    path('', views.render_index_view, name='index')
]