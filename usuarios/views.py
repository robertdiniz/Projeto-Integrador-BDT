from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AlunoForm
from .models import Aluno


def login(request):
    return render(request, "login.html")


def register(request):
    if str(request.method) == "POST":
        form = AlunoForm(request.POST, request.FILES)
        nome_usuario = request.POST["nome_usuario"]
        nome_completo = request.POST["nome_completo"]
        email = request.POST["email"]
        senha = request.POST["senha"]
        matricula = request.FILES["matricula"]
        user = User.objects.create_user(
            username=nome_usuario, email=email, password=senha, is_staff=True
        )

        aluno = Aluno.objects.create(
            nome_completo=nome_completo, user=user, matricula=matricula
        )
        print(matricula)

        if form.is_valid():
            user.save()
            aluno.save()
            return redirect("register")
    else:
        form = AlunoForm()
        print(dir(form))

    return render(request, "register.html", {"form": form})


def tregister(request):
    if str(request.method) == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            return redirect("login")
    else:
        form = AlunoForm()
        print(dir(form))

    return render(request, "tregister.html", {"form": form})
