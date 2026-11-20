from decimal import Decimal

from rest_framework import serializers

from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ("id", "nome", "sinopse", "preco", "imagem", "classificacao", "duracao",)

    def validate_nome(self, value):
        nome_limpo = value.strip()

        if len(nome_limpo) < 2:
            raise serializers.ValidationError(
                "O nome deve possuir pelo menos 2 caracteres."
            )

        return nome_limpo

    def validate_preco(self, value):
        if value <= Decimal("0"):
            raise serializers.ValidationError(
                "O valor do ingresso deve ser maior que zero."
            )
            
        if value > Decimal("35"):
            raise serializers.ValidationError(
            "O valor do ingresso não pode ser maior que R$ 35."
        )

        return value
    
    def validate_duracao(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "A duração deve ser maior que zero."
            )
            
        if value > 300:
            raise serializers.ValidationError(
                "A duração não pode ser maior que 300 minutos."
        )

        return value