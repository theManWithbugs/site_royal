from rest_framework import serializers
from .models import *

class InvestSerializer(serializers.Serializer):
    nome = serializers.CharField()
    total = serializers.IntegerField()