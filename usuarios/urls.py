from django.urls import path
from .views import login, register, logout, settings, perfil, edit, buscar, pedidos_acessos, perfil_selos, trilhas_realizadas

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("settings/", settings, name="settings"),
    path("perfil/<int:id>", perfil, name="perfil"),
    path("edit/", edit, name="edit"),
    path("buscar/", buscar, name="buscar"),
    path("acessos/", pedidos_acessos, name="pedidos_acessos"),
    path("perfil/<int:id>/selos/", perfil_selos, name="perfil_selos"),
    path("perfil/<int:id>/trilhas/", trilhas_realizadas, name="trilhas_realizadas"),
]
