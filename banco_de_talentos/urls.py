from django.urls import path
from .views import index, trilhas, perfil, edit, trilha

urlpatterns = [
    path("", index, name="index"),
    path("trilhas/", trilhas, name="trilhas"),
    path("perfil/", perfil, name="perfil"),
    path("edit/", edit, name="edit"),
    path("trilha/", trilha, name="trilha"),
]
