from django.db import models
from django.contrib.auth.models import User
from banco_de_talentos.models import Trilha, Modulo, Tarefa, Selo


# Alterar para Perfil
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(
        "Nome completo: ", max_length=60, null=False, blank=False
    )
    bio = models.TextField(
        "Biografia:", max_length=150, null=True, default="", blank=True
    )
    foto = models.ImageField(
        "Imagem de Perfil: ", upload_to="perfis", null=True, blank=True
    )
    matricula = models.FileField("Matrícula", upload_to="matriculas")
    perfil_privado = models.BooleanField("Perfil privado", default=False)
    selos = models.ManyToManyField(Selo, blank=True)
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

    xp = models.IntegerField("Pontuação de XP", default=0)
    nivel = models.IntegerField("Nível", default=0)

    def aumentar_xp(self, quantidade):
        self.xp += quantidade
        self.verificar_nivel()
    
    def verificar_nivel(self):
        xp_next_level = 600
        if self.xp >= xp_next_level:
            self.nivel += 1
            self.xp -= xp_next_level
        self.save()

    def __str__(self):
        return self.nome_completo
    

class ConclusaoTarefa(models.Model):
    aluno = models.ForeignKey(Aluno, null=True, on_delete=models.SET_NULL)
    tarefa = models.ForeignKey(Tarefa, null=True, on_delete=models.SET_NULL)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.aluno.nome_completo} - {self.tarefa.nome}'

class ModuloAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    url_projeto = models.URLField(null=True, blank=True)
    concluido = models.BooleanField("Módulo Concluído", default=False)

    def __str__(self):
        return f"{self.modulo} - {self.aluno}"

class ConclusaoTrilha(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE)
    concluido = models.BooleanField("Trilha concluída", default=False)

    def __str__(self):
        return f"{self.trilha} - {self.aluno}"
