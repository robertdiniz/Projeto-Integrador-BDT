# Generated by Django 4.2.6 on 2023-11-08 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0005_aluno_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="foto",
            field=models.ImageField(
                default="",
                null=True,
                upload_to="perfis",
                verbose_name="Imagem de Perfil: ",
            ),
        ),
    ]
