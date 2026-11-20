from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .filters import FilmeFilter
from .models import Filme
from .serializers import FilmeSerializer


class FilmeViewSet(ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilmeFilter