from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.URLField(max_length=500)
    
    def __str__(self):
        return f"{self.nome} - R${self.preco}"