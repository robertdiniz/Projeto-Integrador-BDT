# Generated by Django 4.2.6 on 2023-11-20 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0008_alter_modulo_tarefas"),
        ("usuarios", "0017_alter_aluno_modulos_concluidos"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConclusaoTarefa",
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
                ("concluida", models.BooleanField(default=False)),
                (
                    "aluno",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.aluno",
                    ),
                ),
                (
                    "tarefa",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="banco_de_talentos.tarefa",
                    ),
                ),
            ],
        ),
    ]