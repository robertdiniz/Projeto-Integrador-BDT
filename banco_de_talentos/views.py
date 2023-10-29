from django.shortcuts import render


def index(request):
    print(f"user: {request.user}")
    return render(request, "index.html")
