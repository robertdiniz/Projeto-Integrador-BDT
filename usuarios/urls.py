from django.urls import path
from .views import login, register, tregister, logout, settings, perfil, edit

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("tregister/", tregister, name="tregister"),
    path("logout/", logout, name="logout"),
    path("settings/", settings, name="settings"),
    path("perfil/<int:id>", perfil, name="perfil"),
    path("edit/", edit, name="edit"),
]
