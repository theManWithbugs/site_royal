from rest_framework import serializers
from .models import *

class InvestSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Investimentos
        fields = '__all__'