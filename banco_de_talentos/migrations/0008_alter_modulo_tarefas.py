# Generated by Django 4.2.6 on 2023-11-16 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0007_alter_trilha_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modulo",
            name="tarefas",
            field=models.ManyToManyField(
                blank=True,
                default="",
                related_name="tarefas",
                to="banco_de_talentos.tarefa",
            ),
        ),
    ]
