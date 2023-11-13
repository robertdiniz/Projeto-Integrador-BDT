from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(
        "Nome completo: ", max_length=60, null=False, blank=False
    )
    bio = models.CharField(
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

    def get_redes_sociais(self):
        return [
            (self.linkedin, "caminho/para/linkedin.svg"),
            (self.github, "caminho/para/github.svg"),
            (self.discord, "caminho/para/discord-normal.svg"),
            (self.instagram, "caminho/para/instagram-normal.svg"),
            (self.whatsapp, "caminho/para/wpp-normal.svg"),
        ]

    def __str__(self):
        return self.nome_completo
