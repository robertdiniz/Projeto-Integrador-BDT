from django.shortcuts import render, HttpResponse, redirect
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
    modulos = trilha.modulos.all()
    form = ModuloRepositorioForm()
    form_concluido = ModuloConcluidoForm()

    if request.method == "POST":
        
        if 'modulo_selecionado' in request.POST:
            nome_modulo = request.POST.get('modulo_selecionado')
            modulo = Modulo.objects.get(nome=nome_modulo)
            url = request.POST.get('url_projeto')
            modulo_aluno = ModuloAluno.objects.create(aluno=user.aluno, modulo=modulo, url_projeto=url, concluido=True)
            modulo_aluno.save()
        elif 'modulo_concluir' in request.POST:
            nome_modulo = request.POST.get('modulo_concluir')
            modulo = Modulo.objects.get(nome=nome_modulo)
            modulo_aluno = ModuloAluno.objects.create(aluno=user.aluno, modulo=modulo, concluido=True)
            modulo_aluno.save()

    return render(request, "trilha.html", {'trilha': trilha, 'modulos': modulos, 'form': form, 'form_concluido': form_concluido})



def teste(request):
    
    user = request.user

    trilha = user.aluno.trilha_atual
    modulos = trilha.modulos.all()
    
    for modulo in modulos:
        print(modulo.tarefas.all())

    return render(request, "teste.html", {'trilha': trilha, 'modulos': modulos})
