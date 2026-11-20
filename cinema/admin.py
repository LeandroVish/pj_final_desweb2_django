from django.contrib import admin

from .models import Filme

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "classificacao", "duracao",)

    search_fields = ("nome",)
    list_filter = ("classificacao",)