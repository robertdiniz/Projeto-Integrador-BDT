from django.contrib import admin
from .models import Aluno, ConclusaoTarefa, Projeto


admin.site.register(Aluno)
admin.site.register(ConclusaoTarefa)
admin.site.register(Projeto)
