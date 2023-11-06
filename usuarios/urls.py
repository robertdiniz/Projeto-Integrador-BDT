from django.urls import path
from .views import login, register, tregister, logout, settings

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("tregister/", tregister, name="tregister"),
    path("logout/", logout, name="logout"),
    path("settings/", settings, name="settings"),
    path("settings/", settings, name="settings"),
]
