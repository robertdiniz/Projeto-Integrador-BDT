# Generated by Django 4.2.6 on 2023-11-22 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco_de_talentos', '0010_tarefa_descricao'),
        ('usuarios', '0020_projeto_url_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='aluno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.aluno'),
        ),
        migrations.AlterUniqueTogether(
            name='projeto',
            unique_together={('aluno', 'modulo')},
        ),
    ]
