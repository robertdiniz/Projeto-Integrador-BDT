# Generated by Django 4.1.6 on 2023-11-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0013_alter_modulo_tarefas"),
    ]

    operations = [
        migrations.CreateModel(
            name="Selo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=15, verbose_name="Nome do selo")),
                (
                    "selo_normal",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="selos/",
                        verbose_name="Imagem do selo",
                    ),
                ),
                (
                    "selo_bloqueado",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="selos/",
                        verbose_name="Imagem do selo bloqueado",
                    ),
                ),
                (
                    "selo_desbloqueado",
                    models.ImageField(
                        blank=True,
                        default="",
                        null=True,
                        upload_to="selos/",
                        verbose_name="Imagem do selo desbloqueado",
                    ),
                ),
            ],
        ),
    ]
