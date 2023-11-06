from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import AlunoForm
from .models import Aluno
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_sistema
from django.contrib.auth import logout as logout_sistema


def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if str(request.method) == "POST":
            email = request.POST.get("email")
            senha = request.POST.get("senha")
            existe = User.objects.filter(email=email).exists()
            if existe:
                usuario = User.objects.get(email=email)
                user = authenticate(request, username=usuario.username, password=senha)
                if user is not None:
                    login_sistema(request, user)
                    return HttpResponse(f"Usuário logado!<br>")
            else:
                return HttpResponse(f"Usuário não existe<br>{existe}")

    return render(request, "login.html")


def logout(request):
    logout_sistema(request)
    return redirect("login")


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
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
        if form.is_valid():
            user.save()
            aluno.save()
            return redirect("register")
    else:
        form = AlunoForm()
    return render(request, "register.html", {"form": form})


def settings(request):
    
    

    return render(request, "settings.html")


def tregister(request):
    if str(request.method) == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            return redirect("login")
    else:
        form = AlunoForm()
        print(dir(form))

    return render(request, "tregister.html", {"form": form})
