# Generated by Django 4.2.6 on 2023-11-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0001_initial"),
        ("usuarios", "0011_alter_aluno_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="trilha",
            field=models.ManyToManyField(
                blank=True, default="", null=True, to="banco_de_talentos.trilha"
            ),
        ),
    ]