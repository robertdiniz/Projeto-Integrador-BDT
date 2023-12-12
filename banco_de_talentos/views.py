from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Trilha, Tarefa
from usuarios.models import ModuloAluno, Modulo, ConclusaoTrilha
from .forms import ModuloRepositorioForm, ModuloConcluidoForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

@login_required(login_url='login')
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
        if user.aluno.trilha_atual:
            return redirect('trilha')
        trilhas_concluidas = ConclusaoTrilha.objects.filter(aluno=user.aluno, concluido=True).values_list('trilha', flat=True)
        trilhas_disponiveis = Trilha.objects.exclude(id__in=trilhas_concluidas)
        trilhas = Trilha.objects.all()

        context = {
            "trilhas": trilhas,
            "trilhas_disponiveis": trilhas_disponiveis
        }

        return render(request, "trilhas.html", context)

@login_required(login_url='login')
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

    todos_modulos_concluidos = ModuloAluno.objects.filter(aluno=user.aluno, modulo__in=modulos, concluido=True).count() == modulos.count()

    if request.method == "POST":
        
        if 'modulo_selecionado' in request.POST:
            nome_modulo = request.POST.get('modulo_selecionado')
            modulo = Modulo.objects.get(nome=nome_modulo)
            url = request.POST.get('url_projeto')
            modulo_aluno = ModuloAluno.objects.create(aluno=user.aluno, modulo=modulo, url_projeto=url, concluido=True)
            modulo_aluno.save()
            selos_do_modulo = modulo.selos.all()
            user.aluno.selos.add(*selos_do_modulo)
            user.aluno.aumentar_xp(100)
            return redirect('trilha')
        
        elif 'modulo_concluir' in request.POST:
            nome_modulo = request.POST.get('modulo_concluir')
            modulo = Modulo.objects.get(nome=nome_modulo)
            modulo_aluno = ModuloAluno.objects.create(aluno=user.aluno, modulo=modulo, concluido=True)
            modulo_aluno.save()
            selos_do_modulo = modulo.selos.all()
            user.aluno.selos.add(*selos_do_modulo)
            user.aluno.aumentar_xp(100)
            return redirect('trilha')
        
        elif 'trilha_concluir' in request.POST:
            trilha_concluida = ConclusaoTrilha.objects.create(aluno=user.aluno, trilha=trilha, concluido=True)
            trilha_concluida.save()
            user.aluno.trilha_atual = None
            user.aluno.aumentar_xp(1500)
            return redirect('trilhas')
        
    context = {
        'trilha': trilha, 
        'modulos': modulos, 
        'form': form, 
        'form_concluido': form_concluido, 
        "modulos_concluidos": modulos_aluno,
        "todos_modulos_concluidos": todos_modulos_concluidos
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

