from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import (
    AlunoForm,
    AlunoRedesSociaisForm,
    AlunoBioGrafiaForm,
    AlunoChangeEmailForm,
    AlunoChangePasswordForm,
    AlunoChangePerfilVisibility
)
from .models import Aluno
from banco_de_talentos.models import Trilha
from django.contrib.auth import authenticate, update_session_auth_hash
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


"""
    -*-* Settings -*-*
    - Validar as senhas (?)
"""


def settings(request):
    user = request.user

    if str(request.method) == "POST":
        if "email" in request.POST:
            form_change_email = AlunoChangeEmailForm(request.POST, instance=user)
            if form_change_email.is_valid():
                form_change_email.save()
                return HttpResponse("E-mail alterado com sucesso!")
        if "submit_change_password" in request.POST:
            form_change_password = AlunoChangePasswordForm(request.POST)

            if form_change_password.is_valid():
                new_password = form_change_password.cleaned_data["new_password"]
                confirm_password = form_change_password.cleaned_data["confirm_password"]
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                return HttpResponse("Senha alterada com sucesso!")
        if "submit_change_visibility" in request.POST:
            form_change_visibility = AlunoChangePerfilVisibility(request.POST, instance=user.aluno)
            if form_change_visibility.is_valid():
                form_change_visibility.save()
                return redirect('settings')


    print(AlunoChangePerfilVisibility)

    context = {
        "id_atual": user.id,
        "form_change_password": AlunoChangePasswordForm(),
        "form_change_visibility": AlunoChangePerfilVisibility(instance=user.aluno)
    }
    
    return render(request, "settings.html", context)


def perfil(request, id):

    user = request.user
    aluno = Aluno.objects.get(id=id)

    # Verificação da visibilidade do perfil do aluno e comparação se o aluno é o atual.
    if aluno.perfil_privado and user.aluno.id != aluno.id:
        return HttpResponse(f"O perfil {aluno.nome_completo} é privado!")
    
    busca = request.POST.get("nome")

    if busca:
        return redirect("buscar")

    context = {"perfil": perfil, "aluno": aluno}

    return render(request, "perfil.html", context)


def edit(request):
    user = request.user

    if str(request.method) == "POST":
        if "photo" in request.FILES:
            photo = request.FILES["photo"]
            aluno = Aluno.objects.get(nome_completo=user.aluno.nome_completo)
            aluno.foto = photo
            aluno.save()
            return redirect("edit")

        if "submit_redes_sociais" in request.POST:
            form_redes_sociais = AlunoRedesSociaisForm(
                request.POST, instance=user.aluno
            )
            if form_redes_sociais.is_valid():
                form_redes_sociais.save()
                return redirect("edit")

        if "submit_biografia" in request.POST:
            form_biografia = AlunoBioGrafiaForm(request.POST, instance=user.aluno)
            if form_biografia.is_valid():
                form_biografia.save()
                return redirect("edit")

    else:
        form_redes_sociais = AlunoRedesSociaisForm(instance=user.aluno)
        form_biografia = AlunoBioGrafiaForm(instance=user.aluno)

        return render(
            request,
            "edit.html",
            {"form_rede_social": form_redes_sociais, "form_biografia": form_biografia},
        )


def buscar(request):
    nome = request.GET.get("nome")

    if nome:
        perfis = Aluno.objects.filter(nome_completo__icontains=nome, user__is_active=True).all()

        context = {"perfis": perfis}

        return render(request, "search.html", context)
    else:
        perfis = Aluno.objects.filter(user__is_active=True).all()

        context = {"perfis": perfis}

        return render(request, "search.html", context)


def pedidos_cadastro(request):

    usuarios = User.objects.filter(is_active=False)
    email = request.POST.get('active-account')

    if email:
        usuario = User.objects.get(email=email)
        usuario.is_active = True
        usuario.save()
        return redirect('pedidos_cadastro')

    return render(request, 'requests.html', {"usuarios": usuarios})