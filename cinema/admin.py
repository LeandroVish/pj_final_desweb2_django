from django.contrib import admin

from .models import Filme

@admin.register(Filme)
class MovieAdm(admin.ModelAdmin):
    list_display = ("id", "nome", "preco")
    search_fields = ("nome", )