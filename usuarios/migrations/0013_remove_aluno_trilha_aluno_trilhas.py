# Generated by Django 4.2.6 on 2023-11-14 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0002_tarefa_alter_trilha_nome_modulo"),
        ("usuarios", "0012_aluno_trilha"),
    ]

    operations = [
        migrations.RemoveField(model_name="aluno", name="trilha",),
        migrations.AddField(
            model_name="aluno",
            name="trilhas",
            field=models.ManyToManyField(
                blank=True,
                default="",
                null=True,
                related_name="alunos",
                to="banco_de_talentos.trilha",
            ),
        ),
    ]