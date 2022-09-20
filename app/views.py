from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def horario_atual(request):
    horario_atual = datetime.datetime.now()
    return render(request, 'lista_horario.html', context={'horario': horario_atual})
