from django import forms

class ClienteForm(forms.Form):
    nome = forms.CharField(label="Nome do cliente", max_length=100)
    idade = forms.IntegerField(label="Idade do cliente")
    data_nascimento = forms.DateField(label="Data de nascimento do cliente")
    is_ativo = forms.BooleanField(label="Se o cliente está ativo")