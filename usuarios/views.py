from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as login_sistema
from django.contrib.auth import logout as logout_sistema
from django.contrib.auth.decorators import login_required
from .models import Perfil, SelosAluno
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
                if not len(senha) > 7:
                    messages.error(request, "Senha deve conter no mínimo 8 dígitos.")
                    return redirect('login')
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

        if matricula and not matricula.name.lower().endswith('.pdf'):
            messages.error(request, 'Matrícula deve ser no formato ".pdf".')
            return redirect('register')

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

        if not len(senha) > 7:
            messages.error(request, "Senha com menos de 8 dígitos.")
            return redirect('register')

        user = User.objects.create_user(
            username=nome_usuario, email=email, password=senha, is_active=False
        )
        aluno = Perfil.objects.create(
            nome_completo=nome_completo, user=user, matricula=matricula
        )
        if form.is_valid():
            user.save()
            aluno.save()
            messages.success(request, "Conta criada! Aguarde seu acesso ser liberado ;)")
            return redirect("login")
    else:
        form = AlunoForm()
    return render(request, "register.html", {"form": form, "usuarios_inativos": usuarios_inativos()})


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
                messages.success(request, 'Email alterado com sucesso!')
                return redirect("settings")
        if "submit_change_password" in request.POST:
            form_change_password = AlunoChangePasswordForm(request.POST)

            if form_change_password.is_valid():
                new_password = form_change_password.cleaned_data["new_password"]
                confirm_password = form_change_password.cleaned_data["confirm_password"]
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Senha alterada com sucesso!")
                return redirect("settings")
        if "submit_change_visibility" in request.POST:
            form_change_visibility = AlunoChangePerfilVisibility(request.POST, instance=user.perfil)
            if form_change_visibility.is_valid():
                form_change_visibility.save()
                return redirect('settings')

    context = {
        "id_atual": user.id,
        "form_change_password": AlunoChangePasswordForm(),
        "form_change_visibility": AlunoChangePerfilVisibility(instance=user.perfil),
        "trilhas": user.perfil.trilhas,
        "usuarios_inativos": usuarios_inativos(),
    }
    
    return render(request, "settings.html", context)

@login_required(login_url='login')
def perfil(request, id):

    user = request.user
    aluno = Perfil.objects.get(id=id)
    trilhas_concluidas_aluno = ConclusaoTrilha.objects.filter(perfil=aluno)[:2]
    selos_do_aluno = SelosAluno.objects.filter(perfil=aluno).order_by('-data_conquistada')[:15]

    proprio_perfil = user.is_authenticated and user.perfil.id == aluno.id

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
        "usuarios_inativos": usuarios_inativos(),
    }

    return render(request, "perfil.html", context)

@login_required(login_url='login')
def edit(request):
    user = request.user

    if str(request.method) == "POST":
        if "photo" in request.FILES:
            photo = request.FILES["photo"]
            aluno = Perfil.objects.get(nome_completo=user.perfil.nome_completo)
            aluno.foto = photo
            aluno.save()
            messages.success(request, "Foto alterada!")
            return redirect("edit")

        if "submit_redes_sociais" in request.POST:
            form_redes_sociais = AlunoRedesSociaisForm(
                request.POST, instance=user.perfil
            )
            if form_redes_sociais.is_valid():
                form_redes_sociais.save()
                messages.success(request, "Redes sociais alteradas!")
                return redirect("edit")

        if "submit_biografia" in request.POST:
            form_biografia = AlunoBioGrafiaForm(request.POST, instance=user.perfil)
            if form_biografia.is_valid():
                form_biografia.save()
                messages.success(request, "Biografia alterada!")
                return redirect("edit")

    else:
        form_redes_sociais = AlunoRedesSociaisForm(instance=user.perfil)
        form_biografia = AlunoBioGrafiaForm(instance=user.perfil)

        return render(
            request,
            "edit.html",
            {
                "form_rede_social": form_redes_sociais,
                "form_biografia": form_biografia,
                "usuarios_inativos": usuarios_inativos(),
            },
        )

@login_required(login_url='login')
def buscar(request):

    nome = request.GET.get("nome")

    if nome:
        perfis = Perfil.objects.filter(nome_completo__icontains=nome, user__is_active=True).all()

        p = Paginator(perfis, 5)
        page_number = request.GET.get("page")
        page_obj = p.get_page(page_number)

        context = {
            "perfis": perfis,
            "page_obj": page_obj,
        }

        return render(request, "search.html", context)
    
    perfis = Perfil.objects.filter(user__is_active=True).all()

    p = Paginator(perfis, 5)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)

    context = {
        "perfis": perfis,
        "page_obj": page_obj,
        "usuarios_inativos": usuarios_inativos(),
    }

    return render(request, "search.html", context)

@login_required(login_url='login')
def busca_filtrada(request):
        
    nome = request.GET.get("nome")

    if nome:
        perfis = Perfil.objects.filter(nome_completo__icontains=nome, user__is_active=True).all()

        context = {
            "perfis": perfis,
            "usuarios_inativos": usuarios_inativos(),
        }

        return render(request, "search.html", context)
    else:
        perfis = Perfil.objects.filter(user__is_active=True).all()

        context = {
            "perfis": perfis,
            "usuarios_inativos": usuarios_inativos(),
        }

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
    return render(request, 'requests.html', {"usuarios": usuarios, "usuarios_inativos": usuarios_inativos()})

@login_required(login_url='login')
def perfil_selos(request, id):
    aluno = Perfil.objects.get(id=id)
    selos_do_aluno = SelosAluno.objects.filter(perfil=aluno)

    context = {
        "aluno": aluno,
        "selos_do_aluno": selos_do_aluno,
        "usuarios_inativos": usuarios_inativos(),
    }

    return render(request, 'selos.html', context)

@login_required(login_url='login')
def trilhas_realizadas(request, id):
    aluno = Perfil.objects.get(id=id)
    trilhas_realizadas = ConclusaoTrilha.objects.filter(perfil=aluno)

    context = {
        "aluno": aluno,
        "trilhas_realizadas": trilhas_realizadas,
        "usuarios_inativos": usuarios_inativos(),
    }

    return render(request, 'aluno-trilhas.html', context)


def usuarios_inativos():
    usuarios_inativos = User.objects.filter(is_active=False).count()
    return usuarios_inativos