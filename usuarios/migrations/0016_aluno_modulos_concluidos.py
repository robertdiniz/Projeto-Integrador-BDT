# Generated by Django 4.2.6 on 2023-11-16 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0008_alter_modulo_tarefas"),
        ("usuarios", "0015_aluno_trilha_atual"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="modulos_concluidos",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="modulos_concluidos",
                to="banco_de_talentos.modulo",
            ),
        ),
    ]