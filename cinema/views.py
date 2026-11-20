from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .filters import FilmeFilter
from .models import Filme
from .serializers import FilmeSerializer
from .pagination import FilmePagination


class FilmeViewSet(ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilmeFilter
    ordering_fields = ("nome", "preco")
    ordering = ("id",)
    search_fields = ("nome",)
    pagination_class = FilmePagination