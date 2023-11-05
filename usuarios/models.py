from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(
        "Nome completo: ", max_length=60, null=False, blank=False
    )
    matricula = models.FileField("Matrícula", upload_to="matriculas")
