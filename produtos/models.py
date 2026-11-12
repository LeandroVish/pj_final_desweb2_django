from django.db import models

class Movies(models.Model):
    nome = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='filmes/panico.jpg')
    
    def __str__(self):
        return f"{self.nome} - R${self.preco} - {self.sinopse}"