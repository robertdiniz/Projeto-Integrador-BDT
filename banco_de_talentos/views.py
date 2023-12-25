from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Trilha, Tarefa
from usuarios.models import ModuloAluno, Modulo, ConclusaoTrilha, ConclusaoTarefa, SelosAluno
from .forms import ModuloRepositorioForm, ModuloConcluidoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.views import usuarios_inativos

def index(request):

    if request.user.is_authenticated:
        return redirect("trilha")

    return render(request, "index.html")

@login_required(login_url='login')
def trilhas(request):

    user = request.user


    if request.method == "POST":
        trilha = request.POST.get("trilha")
        trilha_escolhida = Trilha.objects.get(nome=trilha)
        user.perfil.trilhas.add(trilha_escolhida)
        user.perfil.trilha_atual = trilha_escolhida
        user.perfil.save()
        return redirect("trilha")
    else:
        if user.perfil.trilha_atual:
            return redirect('trilha')
        trilhas_concluidas = ConclusaoTrilha.objects.filter(perfil=user.perfil, concluido=True).values_list('trilha', flat=True)
        trilhas_disponiveis = Trilha.objects.exclude(id__in=trilhas_concluidas)
        trilhas = Trilha.objects.all()

        context = {
            "trilhas": trilhas,
            "trilhas_disponiveis": trilhas_disponiveis,
            "usuarios_inativos": usuarios_inativos(),
        }

        return render(request, "trilhas.html", context)

@login_required(login_url='login')
def trilha(request):

    user = request.user
    trilha = user.perfil.trilha_atual

    if trilha is None:
        return redirect('trilhas')

    modulos = trilha.modulos.all()
    form = ModuloRepositorioForm()
    form_concluido = ModuloConcluidoForm()
    modulos_aluno = []

    for modulo in modulos:
        modulo_concluido = ModuloAluno.objects.filter(perfil=user.perfil, modulo=modulo, concluido=True).exists()
        if modulo_concluido:
            modulo_concluido = Modulo.objects.get(nome=modulo.nome)
            modulos_aluno.append(modulo_concluido)

    todos_modulos_concluidos = ModuloAluno.objects.filter(perfil=user.perfil, modulo__in=modulos, concluido=True).count() == modulos.count()
    
    # Tarefas concluidas pelo aluno
    tarefas_concluidas_aluno = []

    todas_tarefas_concluidas = ConclusaoTarefa.objects.filter(perfil=user.perfil, concluida=True)

    for tarefa in todas_tarefas_concluidas:
        tarefa_concluida = Tarefa.objects.get(id=tarefa.tarefa.id) 
        tarefas_concluidas_aluno.append(tarefa_concluida)



    if request.method == "POST":
        
        if 'modulo_selecionado' in request.POST:
            nome_modulo = request.POST.get('modulo_selecionado')
            modulo = Modulo.objects.get(nome=nome_modulo)
            url = request.POST.get('url_projeto')
            modulo_aluno = ModuloAluno.objects.create(perfil=user.perfil, modulo=modulo, url_projeto=url, concluido=True)
            modulo_aluno.save()
            selos_do_modulo = modulo.selos.all()
            for selo in selos_do_modulo:
                SelosAluno.objects.create(perfil=user.perfil, selo=selo)
            user.perfil.aumentar_xp(500)
            return redirect('trilha')
        
        elif 'task-concluida' in request.POST:
            tarefa_enviada = request.POST.getlist('task-concluida')
            tarefa_id = tarefa_enviada[0]
            tarefa = Tarefa.objects.get(id=tarefa_id)
            existe_tarefa_concluida = ConclusaoTarefa.objects.filter(perfil=user.perfil, tarefa=tarefa, concluida=True).exists()
            if existe_tarefa_concluida:
                tarefa_concluida = ConclusaoTarefa.objects.get(perfil=user.perfil, tarefa=tarefa, concluida=True)
                tarefa_concluida.delete()
                user.perfil.xp -= 100
                user.perfil.save()
                messages.error(request, 'Você desmarcou a tarefa, perdeu 100 XP!')
                return redirect('trilha')
            tarefa_concluida = ConclusaoTarefa.objects.create(perfil=user.perfil, tarefa=tarefa, concluida=True)
            tarefa_concluida.save()
            user.perfil.aumentar_xp(100)
            messages.success(request, 'Você ganhou 100 de XP!')
            return redirect('trilha')
            
        elif 'modulo_concluir' in request.POST:
            nome_modulo = request.POST.get('modulo_concluir')
            modulo = Modulo.objects.get(nome=nome_modulo)
            modulo_aluno = ModuloAluno.objects.create(perfil=user.perfil, modulo=modulo, concluido=True)
            modulo_aluno.save()
            selos_do_modulo = modulo.selos.all()
            for selo in selos_do_modulo:
                SelosAluno.objects.create(perfil=user.perfil, selo=selo)
            user.perfil.aumentar_xp(500)
            return redirect('trilha')
        
        elif 'trilha_concluir' in request.POST:
            trilha_concluida = ConclusaoTrilha.objects.create(perfil=user.perfil, trilha=trilha, concluido=True)
            trilha_concluida.save()
            user.perfil.trilha_atual = None
            user.perfil.aumentar_xp(1500)
            return redirect('trilhas')

    context = {
        'trilha': trilha, 
        'modulos': modulos, 
        'form': form, 
        'form_concluido': form_concluido, 
        "modulos_concluidos": modulos_aluno,
        "todos_modulos_concluidos": todos_modulos_concluidos,
        "todas_tarefas_concluidas": todas_tarefas_concluidas,
        "tarefas_concluidas_aluno": tarefas_concluidas_aluno,
        "usuarios_inativos": usuarios_inativos(),
    }

    return render(request, "trilha.html", context)



