# Generated by Django 4.2.6 on 2023-11-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0008_alter_aluno_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="discord",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="discord:"
            ),
        ),
        migrations.AddField(
            model_name="aluno",
            name="github",
            field=models.URLField(
                blank=True, default="", null=True, verbose_name="Github:"
            ),
        ),
        migrations.AddField(
            model_name="aluno",
            name="instagram",
            field=models.URLField(
                blank=True, default="", null=True, verbose_name="Instagram:"
            ),
        ),
        migrations.AddField(
            model_name="aluno",
            name="linkedin",
            field=models.URLField(
                blank=True, default="", null=True, verbose_name="Linkedin:"
            ),
        ),
        migrations.AddField(
            model_name="aluno",
            name="whatsapp",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="Whatsapp:"
            ),
        ),
    ]
