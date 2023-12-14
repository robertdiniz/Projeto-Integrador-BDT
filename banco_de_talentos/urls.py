from django.urls import path
from .views import index, trilhas, trilha, not_found

urlpatterns = [
    path("", index, name="index"),
    path("trilhas/", trilhas, name="trilhas"),
    path("trilha/", trilha, name="trilha"),
    path("404/", not_found, name="not_found"),
]
