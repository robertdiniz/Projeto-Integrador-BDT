from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def trilhas(request):
    return render(request, "trilhas.html")


def perfil(request):
    return render(request, "perfil.html")


def edit(request):
    return render(request, "edit.html")


def trilha(request):
    return render(request, "trilha.html")
