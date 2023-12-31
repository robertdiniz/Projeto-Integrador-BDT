# Generated by Django 4.2.6 on 2023-11-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0009_aluno_discord_aluno_github_aluno_instagram_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aluno",
            name="discord",
            field=models.CharField(
                blank=True,
                default="",
                max_length=50,
                null=True,
                verbose_name="discord:",
            ),
        ),
        migrations.AlterField(
            model_name="aluno",
            name="whatsapp",
            field=models.CharField(
                blank=True,
                default="",
                max_length=10,
                null=True,
                verbose_name="Whatsapp:",
            ),
        ),
    ]
