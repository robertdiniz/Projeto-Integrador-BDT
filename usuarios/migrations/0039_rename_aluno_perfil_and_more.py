# Generated by Django 4.2.6 on 2023-12-24 20:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("banco_de_talentos", "0016_modulo_selos"),
        (
            "usuarios",
            "0038_remove_aluno_selos_alter_conclusaotrilha_concluido_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(old_name="Aluno", new_name="Perfil",),
        migrations.RenameField(
            model_name="conclusaotarefa", old_name="aluno", new_name="perfil",
        ),
        migrations.RenameField(
            model_name="conclusaotrilha", old_name="aluno", new_name="perfil",
        ),
        migrations.RenameField(
            model_name="moduloaluno", old_name="aluno", new_name="perfil",
        ),
        migrations.RenameField(
            model_name="selosaluno", old_name="aluno", new_name="perfil",
        ),
        migrations.AlterUniqueTogether(
            name="conclusaotarefa", unique_together={("perfil", "tarefa")},
        ),
        migrations.AlterUniqueTogether(
            name="conclusaotrilha", unique_together={("perfil", "trilha")},
        ),
        migrations.AlterUniqueTogether(
            name="moduloaluno", unique_together={("perfil", "modulo")},
        ),
        migrations.AlterUniqueTogether(
            name="selosaluno", unique_together={("perfil", "selo")},
        ),
    ]
