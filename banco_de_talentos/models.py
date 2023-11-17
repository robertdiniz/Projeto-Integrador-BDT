from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(
        "Nome da tarefa:", max_length=50, null=True, blank=True, default=""
    )

    def __str__(self):
        return self.nome


class Modulo(models.Model):
    nome = models.CharField(
        "Nome do módulo:", max_length=50, null=True, blank=True, default=""
    )

    tarefas = models.ManyToManyField(
        Tarefa, related_name="tarefas", default="", blank=True
    )

    def __str__(self):
        return self.nome


class Trilha(models.Model):
    nome = models.CharField(
        "Nome da trilha:", max_length=50, null=True, blank=True, default=""
    )

    imagem = models.ImageField(
        "Imagem da trilha", upload_to="trilhas/", null=True, default="", blank=True
    )

    modulos = models.ManyToManyField(
        Modulo, related_name="trilhas", default="", blank=True
    )

    def __str__(self):
        return self.nome
