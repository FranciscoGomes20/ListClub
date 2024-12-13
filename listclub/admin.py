from django.contrib import admin
from .models import Categorias, Listas, Status, Diretor, Itens, Generos

# Register your models here.
@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ['nome']

@admin.register(Listas)
class ListasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ['nome']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Itens)
class ItensAdmin(admin.ModelAdmin):
    list_display = ('ordem', 'nome', 'descricao')
    search_fields = ('ordem', 'nome')

@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
