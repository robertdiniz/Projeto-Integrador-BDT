from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as login_sistema
from django.contrib.auth import logout as logout_sistema
from django.contrib.auth.decorators import login_required
from .models import Aluno, SelosAluno
from banco_de_talentos.models import Trilha
from usuarios.models import ConclusaoTrilha, SelosAluno
from .forms import (
    AlunoForm,
    AlunoRedesSociaisForm,
    AlunoBioGrafiaForm,
    AlunoChangeEmailForm,
    AlunoChangePasswordForm,
    AlunoChangePerfilVisibility
)
import re


def login(request):
    if request.user.is_authenticated:
        return redirect("trilha")
    else:
        if str(request.method) == "POST":
            email = request.POST.get("email")
            senha = request.POST.get("senha")
            existe = User.objects.filter(email=email).exists()
            if existe:
                usuario = User.objects.get(email=email)
                user = authenticate(request, username=usuario.username, password=senha)
                
                if user is not None and user.is_active:
                    login_sistema(request, user)
                    return redirect("trilha")
                else:
                    messages.error(request, "Sua conta não tem acesso ao sistema.")
                    return redirect("login")
            else:
                messages.error(request, "Esse usuário não existe!")
                return redirect('login')


    return render(request, "login.html")


def logout(request):
    logout_sistema(request)
    return redirect("login")


def register(request):
    if request.user.is_authenticated:
        return redirect("trilha")
    if str(request.method) == "POST":
        form = AlunoForm(request.POST, request.FILES)
        nome_usuario = request.POST["nome_usuario"]
        nome_completo = request.POST["nome_completo"]
        email = request.POST["email"]
        senha = request.POST["senha"]
        matricula = request.FILES["matricula"]

        # Validar nome de usuário
        def validar_nome_usuario(nome_usuario):
            if not re.match("^[a-zA-Z0-9_-]+$", nome_usuario):
                return False, "O nome de usuário pode conter apenas letras, números, underscores (_) e hifens (-)."
            return True, ""
            
        nome_usuario_valido, mensagem_erro = validar_nome_usuario(nome_usuario)

        if not nome_usuario_valido:
            messages.error(request, mensagem_erro)
            return redirect('register')

        # Verificar se já existe nome de usuário ou email
        nome_de_usuario_existe = User.objects.filter(username=nome_usuario).exists()
        email_existe = User.objects.filter(username=nome_usuario).exists()

        if nome_de_usuario_existe or email_existe:
            messages.error(request, "Nome de usuário ou email já existe!")
            return redirect('register')

        user = User.objects.create_user(
            username=nome_usuario, email=email, password=senha, is_active=False
        )
        aluno = Aluno.objects.create(
            nome_completo=nome_completo, user=user, matricula=matricula
        )
        if form.is_valid():
            user.save()
            aluno.save()
            messages.success(request, "Conta criada! Aguarde seu acesso ser liberado ;)")
            return redirect("login")
    else:
        form = AlunoForm()
    return render(request, "register.html", {"form": form})


"""
    -*-* Settings -*-*
    - Validar as senhas (?)
"""

@login_required(login_url='login')
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

    context = {
        "id_atual": user.id,
        "form_change_password": AlunoChangePasswordForm(),
        "form_change_visibility": AlunoChangePerfilVisibility(instance=user.aluno),
        "trilhas": user.aluno.trilhas
    }
    
    return render(request, "settings.html", context)

@login_required(login_url='login')
def perfil(request, id):

    user = request.user
    aluno = Aluno.objects.get(id=id)
    trilhas_concluidas_aluno = ConclusaoTrilha.objects.filter(aluno=aluno)[:2]
    selos_do_aluno = SelosAluno.objects.filter(aluno=aluno).order_by('-data_conquistada')[:15]

    proprio_perfil = user.is_authenticated and user.aluno.id == aluno.id

    # Verificação da visibilidade do perfil do aluno e comparação se o aluno é o atual e se é usuário normal.
    if aluno.perfil_privado and not proprio_perfil and user.is_staff is False: 
        return render(request, "privado.html", {'aluno': aluno})
    
    busca = request.POST.get("nome")

    if busca:
        return redirect("buscar")

    context = {
        "perfil": perfil, 
        "aluno": aluno, 
        "proprio_perfil": proprio_perfil,
        "trilhas_concluidas_aluno": trilhas_concluidas_aluno,
        "selos_do_aluno": selos_do_aluno,
    }

    return render(request, "perfil.html", context)

@login_required(login_url='login')
def edit(request):
    user = request.user

    if str(request.method) == "POST":
        if "photo" in request.FILES:
            photo = request.FILES["photo"]
            aluno = Aluno.objects.get(nome_completo=user.aluno.nome_completo)
            aluno.foto = photo
            aluno.save()
            messages.success(request, "Foto alterada!")
            return redirect("edit")

        if "submit_redes_sociais" in request.POST:
            form_redes_sociais = AlunoRedesSociaisForm(
                request.POST, instance=user.aluno
            )
            if form_redes_sociais.is_valid():
                form_redes_sociais.save()
                messages.success(request, "Redes sociais alteradas!")
                return redirect("edit")

        if "submit_biografia" in request.POST:
            form_biografia = AlunoBioGrafiaForm(request.POST, instance=user.aluno)
            if form_biografia.is_valid():
                form_biografia.save()
                messages.success(request, "Biografia alterada!")
                return redirect("edit")

    else:
        form_redes_sociais = AlunoRedesSociaisForm(instance=user.aluno)
        form_biografia = AlunoBioGrafiaForm(instance=user.aluno)

        return render(
            request,
            "edit.html",
            {"form_rede_social": form_redes_sociais, "form_biografia": form_biografia},
        )

@login_required(login_url='login')
def buscar(request):

    nome = request.GET.get("nome")

    if nome:
        perfis = Aluno.objects.filter(nome_completo__icontains=nome, user__is_active=True).all()

        p = Paginator(perfis, 5)
        page_number = request.GET.get("page")
        page_obj = p.get_page(page_number)

        context = {
            "perfis": perfis,
            "page_obj": page_obj,
        }

        return render(request, "search.html", context)
    
    perfis = Aluno.objects.filter(user__is_active=True).all()

    p = Paginator(perfis, 5)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)

    context = {
        "perfis": perfis,
        "page_obj": page_obj,
    }

    return render(request, "search.html", context)

@login_required(login_url='login')
def busca_filtrada(request):
        
    nome = request.GET.get("nome")

    if nome:
        perfis = Aluno.objects.filter(nome_completo__icontains=nome, user__is_active=True).all()

        context = {"perfis": perfis}

        return render(request, "search.html", context)
    else:
        perfis = Aluno.objects.filter(user__is_active=True).all()

        context = {"perfis": perfis}

        return render(request, "search.html", context)

@login_required(login_url='login')
def pedidos_acessos(request):

    usuarios = User.objects.filter(is_active=False)

    if request.method == "POST":
        if 'active-account' in request.POST and request.POST['active-account']:
            email = request.POST.get('active-account')
            if email:
                usuario = User.objects.get(email=email)
                usuario.is_active=True
                usuario.save()
                messages.success(request, f"{usuario.username} recebeu acesso ao sistema!")
                return redirect('pedidos_acessos')
        elif 'reject-account' in request.POST and request.POST['reject-account']:
            email = request.POST.get('reject-account')
            if email:
                print('existe!')
                usuario = User.objects.get(email=email)
                messages.success(request, f"{usuario.username} foi rejeitado(a) do sistema!")
                usuario.delete()
                return redirect('pedidos_acessos')
    return render(request, 'requests.html', {"usuarios": usuarios})

@login_required(login_url='login')
def perfil_selos(request, id):
    aluno = Aluno.objects.get(id=id)
    selos_do_aluno = SelosAluno.objects.filter(aluno=aluno)

    context = {
        "aluno": aluno,
        "selos_do_aluno": selos_do_aluno,
    }

    return render(request, 'selos.html', context)

@login_required(login_url='login')
def trilhas_realizadas(request, id):
    aluno = Aluno.objects.get(id=id)
    trilhas_realizadas = ConclusaoTrilha.objects.filter(aluno=aluno)

    context = {
        "aluno": aluno,
        "trilhas_realizadas": trilhas_realizadas,
    }

    return render(request, 'aluno-trilhas.html', context)