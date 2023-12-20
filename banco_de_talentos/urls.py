from django.urls import path
from .views import index, trilhas, trilha

urlpatterns = [
    path("", index, name="index"),
    path("trilhas/", trilhas, name="trilhas"),
    path("trilha/", trilha, name="trilha"),
]
