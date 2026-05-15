from django.urls import path
from agendamientoCitas import views

urlpatterns = [
    path('', views.render_citas, name='citas')
]