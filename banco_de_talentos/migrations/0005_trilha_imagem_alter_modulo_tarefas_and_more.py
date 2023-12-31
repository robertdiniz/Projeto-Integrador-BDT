# Generated by Django 4.2.6 on 2023-11-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0004_alter_trilha_modulos"),
    ]

    operations = [
        migrations.AddField(
            model_name="trilha",
            name="imagem",
            field=models.ImageField(
                default="img/dev.svg",
                null=True,
                upload_to="trilhas/",
                verbose_name="Imagem da trilha",
            ),
        ),
        migrations.AlterField(
            model_name="modulo",
            name="tarefas",
            field=models.ManyToManyField(
                blank=True,
                default="",
                related_name="modulos",
                to="banco_de_talentos.tarefa",
            ),
        ),
        migrations.AlterField(
            model_name="trilha",
            name="modulos",
            field=models.ManyToManyField(
                blank=True,
                default="",
                related_name="trilhas",
                to="banco_de_talentos.modulo",
            ),
        ),
    ]
