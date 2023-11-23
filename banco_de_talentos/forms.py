from django import forms
from django.forms import ModelForm
from usuarios.models import ModuloAluno
from banco_de_talentos.models import Modulo

class ModuloRepositorioForm(ModelForm):
    class Meta:
        model = ModuloAluno
        fields = ['url_projeto']
        widgets = {
            'url_projeto': forms.TextInput(attrs={"placeholder": "Insira o link do repositório...", "id": "url-rep"})
        }

class ModuloConcluidoForm(ModelForm):
    class Meta:
        model = ModuloAluno
        fields = ['concluido']
        widgets = {
            'concluido': forms.HiddenInput(attrs={"id": Modulo })
        }