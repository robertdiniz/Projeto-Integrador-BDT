from django import forms
from .models import Aluno


class AlunoForm(forms.Form):
    nome_usuario = forms.CharField(
        label="Nome de usuário",
        max_length=60,
        widget=forms.TextInput(attrs={"placeholder": "Insira o nome de usuário..."}),
    )
    nome_completo = forms.CharField(
        label="Nome completo",
        max_length=60,
        widget=forms.TextInput(attrs={"placeholder": "Insira o seu nome completo..."}),
    )
    email = forms.EmailField(
        label="Digite seu e-mail",
        widget=forms.TextInput(attrs={"placeholder": "Insira o seu e-mail..."}),
    )
    senha = forms.CharField(
        label="Digite sua senha",
        max_length=60,
        widget=forms.TextInput(attrs={"placeholder": "Insira sua melhor senha..."}),
    )
    matricula = forms.FileField(label="Envie sua matrícula")


class AlunoRedesSociaisForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["linkedin", "github", "discord", "instagram", "whatsapp"]
        widgets = {
            "linkedin": forms.TextInput(
                attrs={"placeholder": "Insira o link do LinkedIn..."}
            ),
            "github": forms.TextInput(
                attrs={"placeholder": "Insira o link do GitHub..."}
            ),
            "whatsapp": forms.TextInput(
                attrs={"placeholder": "Insira o número do WhatsApp..."}
            ),
            "instagram": forms.TextInput(
                attrs={"placeholder": "Insira o nome do Instagram..."}
            ),
            "discord": forms.TextInput(
                attrs={"placeholder": "Insira o ID do Discord..."}
            ),
        }


class AlunoBioGrafiaForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["bio"]
