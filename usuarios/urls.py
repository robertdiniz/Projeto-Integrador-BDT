from django.urls import path
from .views import login, register, logout, settings, perfil, edit, buscar, pedidos_cadastro, busca_filtrada

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("settings/", settings, name="settings"),
    path("perfil/<int:id>", perfil, name="perfil"),
    path("edit/", edit, name="edit"),
    path("buscar/", buscar, name="buscar"),
    path("cadastros/", pedidos_cadastro, name="pedidos_cadastro"),
    path("busca-filtrada/", busca_filtrada, name="busca_filtrada"),
]
