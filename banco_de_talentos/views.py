from django.shortcuts import render, HttpResponse, redirect
from .models import Trilha, Tarefa


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
    
    for modulo in modulos:
        print(modulo.tarefas.all())

    return render(request, "trilha.html", {'trilha': trilha, 'modulos': modulos})


def teste(request):
    
    tarefas = Tarefa.objects.all()

    if request.method == "POST":
        atv = request.POST.get('submit_tarefa')
        print(atv)

    return render(request, "teste.html", {'tarefas': tarefas})
