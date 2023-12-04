from django.db import models

class Selo(models.Model):
    nome = models.CharField("Nome do selo", max_length=15)
    selo_normal = models.FileField("Imagem do selo", upload_to="selos/", null=True, default="", blank=True)
    selo_bloqueado = models.FileField("Imagem do selo bloqueado", upload_to="selos/", null=True, default="", blank=True)
    selo_desbloqueado = models.FileField("Imagem do selo desbloqueado", upload_to="selos/", null=True, default="", blank=True)
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    nome = models.CharField(
        "Nome da tarefa:", max_length=50, null=True, blank=True, default=""
    )

    descricao = models.TextField("Descrição da tarefa", null=True, blank=True)

    def __str__(self):
        return self.nome


class Modulo(models.Model):
    nome = models.CharField(
        "Nome do módulo:", max_length=50, null=True, blank=True, default=""
    )

    requer_projeto = models.BooleanField(default=False)
    concluido = models.BooleanField(default=False)

    selos = models.ManyToManyField(Selo, related_name="selos", blank=True)

    tarefas = models.ManyToManyField(
        Tarefa, related_name="tarefas", blank=True
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

