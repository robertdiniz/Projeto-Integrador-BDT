# Generated by Django 4.1.6 on 2023-11-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banco_de_talentos", "0015_alter_selo_selo_bloqueado_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="modulo",
            name="selos",
            field=models.ManyToManyField(
                blank=True, related_name="selos", to="banco_de_talentos.selo"
            ),
        ),
    ]