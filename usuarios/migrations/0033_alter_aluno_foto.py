# Generated by Django 4.2.6 on 2023-12-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0032_aluno_nivel_aluno_xp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aluno",
            name="foto",
            field=models.ImageField(
                default=False,
                null=True,
                upload_to="perfis",
                verbose_name="Imagem de Perfil: ",
            ),
        ),
    ]