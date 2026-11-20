from django_filters import rest_framework as filters

from .models import Filme


class FilmeFilter(filters.FilterSet):
    preco_minimo = filters.NumberFilter(field_name="preco", lookup_expr="gte")
    preco_maximo = filters.NumberFilter(field_name="preco", lookup_expr="lte")

    class Meta:
        model = Filme
        fields = ("preco_minimo", "preco_maximo")