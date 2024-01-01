from django.urls import path
from .views import *

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", logout, name="logout"),
    path("settings/", SettingsView.as_view(), name="settings"),
    path("perfil/<int:id>", perfil, name="perfil"),
    path("edit/", edit, name="edit"),
    path("buscar/", buscar, name="buscar"),
    path("acessos/", pedidos_acessos, name="pedidos_acessos"),
    path("perfil/<int:id>/selos/", perfil_selos, name="perfil_selos"),
    path("perfil/<int:id>/trilhas/", trilhas_realizadas, name="trilhas_realizadas"),
]
