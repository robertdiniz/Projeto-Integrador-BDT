from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")


def trilhas(request):
    return render(request, "trilhas.html")


def trilha(request):
    return render(request, "trilha.html")


def teste(request):
    if request.method == "POST":
        campo1 = request.POST.get("campo1")
        campo2 = request.POST.get("campo2")


        # Agora você deve obter os dados de ambos os campos
        return HttpResponse(f"Campo 1: {campo1}, Campo 2: {campo2}")

    return render(request, "teste.html")
