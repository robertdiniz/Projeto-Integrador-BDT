# Generated by Django 4.2.6 on 2023-11-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="matricula",
            field=models.FileField(default="", upload_to="", verbose_name="Matrícula"),
            preserve_default=False,
        ),
    ]