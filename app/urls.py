from django.contrib import admin
from django.urls import include, path
from .views import horario_atual, form_cliente

urlpatterns = [
    path('horario_atual', horario_atual),
    path('form_cliente', form_cliente),
]