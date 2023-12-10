from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Trilha, Tarefa
from usuarios.models import ModuloAluno, Modulo
from .forms import ModuloRepositorioForm, ModuloConcluidoForm


def index(request):
    return render(request, "index.html")


def trilhas(request):

    user = request.user

    if request.method == "POST":
        trilha = request.POST.get("trilha")
        trilha_escolhida = Trilha.objects.get(nome=trilha)
        user.aluno.trilhas.add(trilha_escolhida)
        user.aluno.trilha_atual = trilha_escolhida
        user.aluno.save()
        return redirect("trilha")
    else:
        trilhas = Trilha.objects.all()

        return render(request, "trilhas.html", {"trilhas": trilhas})


def trilha(request):

    user = request.user
    trilha = user.aluno.trilha_atual

    if trilha is None:
        return redirect('trilhas')

    modulos = trilha.modulos.all()
    form = ModuloRepositorioForm()
    form_concluido = ModuloConcluidoForm()
    modulos_aluno = []

    for modulo in modulos:
        modulo_concluido = ModuloAluno.objects.filter(aluno=user.aluno, modulo=modulo, concluido=True).exists()
        if modulo_concluido:
            modulo_concluido = Modulo.objects.get(nome=modulo.nome)
            modulos_aluno.append(modulo_concluido)

    if request.method == "POST":
        
        if 'modulo_selecionado' in request.POST:
            nome_modulo = request.POST.get('modulo_selecionado')
            modulo = Modulo.objects.get(nome=nome_modulo)
            url = request.POST.get('url_projeto')
            modulo_aluno = ModuloAluno.objects.create(aluno=user.aluno, modulo=modulo, url_projeto=url, concluido=True)
            modulo_aluno.save()
            selos_do_modulo = modulo.selos.all()
            user.aluno.selos.add(*selos_do_modulo)
            return redirect('trilha')
        
        elif 'modulo_concluir' in request.POST:
            nome_modulo = request.POST.get('modulo_concluir')
            modulo = Modulo.objects.get(nome=nome_modulo)
            modulo_aluno = ModuloAluno.objects.create(aluno=user.aluno, modulo=modulo, concluido=True)
            modulo_aluno.save()
            selos_do_modulo = modulo.selos.all()
            user.aluno.selos.add(*selos_do_modulo)
            return redirect('trilha')
        
    context = {
        'trilha': trilha, 
        'modulos': modulos, 
        'form': form, 
        'form_concluido': form_concluido, 
        "modulos_concluidos": modulos_aluno
    }

    return render(request, "trilha.html", context)



def teste(request):
    
    user = request.user

    trilha = user.aluno.trilha_atual
    modulos = trilha.modulos.all()
    
    for modulo in modulos:
        print(modulo.tarefas.all())

    return render(request, "teste.html", {'trilha': trilha, 'modulos': modulos})


def not_found(request):
    return render(request, '404.html')