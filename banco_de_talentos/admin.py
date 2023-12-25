from django.contrib import admin
from .models import Trilha, Modulo, Tarefa, Selo

# Register your models here.

class TrilhaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trilha, TrilhaAdmin)
admin.site.register(Modulo)
admin.site.register(Tarefa)
admin.site.register(Selo)
