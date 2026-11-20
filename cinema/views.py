from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .filters import FilmeFilter
from .models import Filme
from .pagination import FilmePagination
from .serializers import FilmeSerializer

class FilmeViewSet(ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )

    filterset_class = FilmeFilter

    ordering_fields = ("nome", "preco", "duracao")

    ordering = ("id",)

    search_fields = ("nome","sinopse")

    pagination_class = FilmePagination