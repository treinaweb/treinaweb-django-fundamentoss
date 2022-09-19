from django.contrib import admin
from django.urls import include, path
from .views import horario_atual

urlpatterns = [
    path('horario_atual', horario_atual)
]