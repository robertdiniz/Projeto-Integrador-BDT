from django.contrib import admin
from .models import Aluno, ConclusaoTarefa, ModuloAluno, ConclusaoTrilha


admin.site.register(Aluno)
admin.site.register(ConclusaoTarefa)
admin.site.register(ModuloAluno)
admin.site.register(ConclusaoTrilha)
