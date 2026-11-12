from django.contrib import admin

from .models import Movies

@admin.register(Movies)
class MovieAdm(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco")
    search_fields = ("nome", )