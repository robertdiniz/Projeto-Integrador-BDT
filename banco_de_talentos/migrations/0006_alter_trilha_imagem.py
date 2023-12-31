# Generated by Django 4.2.6 on 2023-11-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0005_trilha_imagem_alter_modulo_tarefas_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trilha",
            name="imagem",
            field=models.ImageField(
                default="",
                null=True,
                upload_to="trilhas/",
                verbose_name="Imagem da trilha",
            ),
        ),
    ]
