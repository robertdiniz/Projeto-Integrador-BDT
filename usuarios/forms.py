from django import forms


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
