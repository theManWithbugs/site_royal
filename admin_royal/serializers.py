from rest_framework import serializers
from .models import *

class InvestSerializer(serializers.Serializer):
    # titulo = serializers.CharField()
    nome = serializers.CharField()
    total = serializers.IntegerField()

class InvestTituloSeria(serializers.Serializer):
    nome = serializers.CharField()
    titulo = serializers.CharField()
    total = serializers.IntegerField()
