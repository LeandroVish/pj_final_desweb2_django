from django_filters import rest_framework as filters

from .models import Filme

class FilmeFilter(filters.FilterSet):
    preco_minimo = filters.NumberFilter(
        field_name="preco",
        lookup_expr="gte"
    )

    preco_maximo = filters.NumberFilter(
        field_name="preco",
        lookup_expr="lte"
    )

    duracao_minima = filters.NumberFilter(
        field_name="duracao",
        lookup_expr="gte"
    )

    duracao_maxima = filters.NumberFilter(
        field_name="duracao",
        lookup_expr="lte"
    )

    classificacao = filters.CharFilter(
        field_name="classificacao"
    )

    class Meta:
        model = Filme
        fields = (
            "preco_minimo",
            "preco_maximo",
            "duracao_minima",
            "duracao_maxima",
            "classificacao",
        )