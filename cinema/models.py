from django.db import models

class Filme(models.Model):
    CLASSIFICACOES = [
        ("L", "Livre"),
        ("10", "10 anos"),
        ("12", "12 anos"),
        ("14", "14 anos"),
        ("16", "16 anos"),
        ("18", "18 anos"),
    ]

    nome = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.URLField(max_length=500)
    classificacao = models.CharField(
        max_length=2,
        choices=CLASSIFICACOES
    )
    duracao = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - R${self.preco} - Tempo:{self.duracao} - Publico{self.classificacao}"