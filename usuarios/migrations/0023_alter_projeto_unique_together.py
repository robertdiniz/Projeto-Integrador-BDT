# Generated by Django 4.2.6 on 2023-11-23 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0022_alter_projeto_modulo"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="projeto", unique_together=set(),),
    ]
