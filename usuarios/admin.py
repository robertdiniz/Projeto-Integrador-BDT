from django.contrib import admin
from .models import Perfil, ConclusaoTarefa, ModuloAluno, ConclusaoTrilha, SelosAluno

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'trilha_atual', 'matricula', )
    list_filter = ('trilha_atual', 'nivel')
    search_fields = ('nome_completo',)

class ModuloAlunoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'modulo',)
    list_filter = ('modulo',)
    search_fields = ('perfil.nome_completo',)

class SelosAlunoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'selo',)
    list_filter = ('selo',)
    search_fields = ('perfil.nome_completo',)

class ConclusaoTarefaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'tarefa',)
    list_filter = ('tarefa',)
    search_fields = ('perfil.nome_completo',)

class ConclusaoTrilhaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'trilha',)
    list_filter = ('trilha',)
    search_fields = ('perfil.nome_completo',)

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(SelosAluno, SelosAlunoAdmin)
admin.site.register(ConclusaoTarefa, ConclusaoTarefaAdmin)
admin.site.register(ModuloAluno, ModuloAlunoAdmin)
admin.site.register(ConclusaoTrilha, ConclusaoTrilhaAdmin)
