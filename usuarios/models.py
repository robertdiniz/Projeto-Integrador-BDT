from django.db import models
from django.contrib.auth.models import User
from banco_de_talentos.models import Trilha, Modulo, Tarefa


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(
        "Nome completo: ", max_length=60, null=False, blank=False
    )
    bio = models.TextField(
        "Biografia:", max_length=150, null=True, default="", blank=True
    )
    foto = models.ImageField(
        "Imagem de Perfil: ", upload_to="perfis", null=True, default="img/aluno.svg"
    )
    matricula = models.FileField("Matrícula", upload_to="matriculas")
    linkedin = models.URLField("Linkedin:", blank=True, null=True, default="")
    github = models.URLField("Github:", blank=True, null=True, default="")
    discord = models.CharField(
        "discord:", blank=True, null=True, default="", max_length=50
    )
    instagram = models.URLField("Instagram:", blank=True, null=True, default="")
    whatsapp = models.CharField(
        "Whatsapp:", blank=True, null=True, default="", max_length=10
    )

    trilhas = models.ManyToManyField(
        Trilha, related_name="alunos", default="", blank=True
    )

    trilha_atual = models.ForeignKey(Trilha, related_name="alunos_em_andamento", blank=True, null=True, on_delete=models.SET_NULL)

    modulos_concluidos = models.ManyToManyField(Modulo, related_name="modulos_concluidos",  blank=True)

    def __str__(self):
        return self.nome_completo

class ConclusaoTarefa(models.Model):
    aluno = models.ForeignKey(Aluno, null=True, on_delete=models.SET_NULL)
    tarefa = models.ForeignKey(Tarefa, null=True, on_delete=models.SET_NULL)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.aluno.nome_completo} - {self.tarefa.nome}'

class Projeto(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    url_projeto = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ['aluno', 'modulo']

    def __str__(self):
        return f"Projeto de {self.aluno} para o módulo {self.modulo}"