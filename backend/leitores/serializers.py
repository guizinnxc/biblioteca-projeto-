from rest_framework import serializers

from .models import Leitor


class LeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = ['id', 'nome', 'email', 'matricula', 'data_cadastro']
