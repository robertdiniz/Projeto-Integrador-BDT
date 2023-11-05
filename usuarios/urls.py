from django.urls import path
from .views import login, register, tregister

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("tregister/", tregister, name="tregister"),
]
