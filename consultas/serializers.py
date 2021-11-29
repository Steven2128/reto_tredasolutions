#Rest Framework
from django.db.models import fields
from rest_framework import serializers
#Models
from .models import Consulta, Ciudad


class CiudadSerializer(serializers.ModelSerializer):
    """Serializer del modelo Ciudad"""
    class Meta:
        model = Ciudad
        fields = '__all__'



class ConsultaSerializer(serializers.ModelSerializer):
    """Serializer del modelo Consulta"""
    class Meta:
        model = Consulta
        fields = '__all__'