from django.urls import path
from .views import index, trilhas, trilha, teste

urlpatterns = [
    path("", index, name="index"),
    path("trilhas/", trilhas, name="trilhas"),
    path("trilha/", trilha, name="trilha"),
    path("teste/", teste, name="teste"),
]
