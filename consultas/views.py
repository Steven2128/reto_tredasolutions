#Rest Framwework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Request
import requests
from datetime import date, datetime
#Django
from django.shortcuts import render
#Serializers
from .serializers import CiudadSerializer, ConsultaSerializer
#Models
from .models import Consulta, Ciudad


class CiudadAPIView(APIView):
    """APIView de Ciudad"""
    def get(self, request, ciudad=None):
        ciudad = str(ciudad).title()
        response = get_consulta(ciudad=ciudad)
        ciudad_obj = Ciudad.objects.filter(nombre=ciudad).first()
        
        """Si no existe la ciudad"""
        if ciudad_obj is None:
            serializer = CiudadSerializer(data = {'nombre': ciudad })
            if serializer.is_valid():
                serializer.save()
                
                ciudad_obj = Ciudad.objects.filter(nombre=ciudad).first()
                temperatura = response['main']['temp']
                humedad = response['main']['humidity']
                velocidad_viento = response['wind']['speed']
                
                serializer_consulta = ConsultaSerializer(data = {
                    'ciudad': ciudad_obj.pk,
                    'temperatura': temperatura,
                    'humedad': humedad,
                    'velocidad_viento': velocidad_viento,
                    'hora_consulta': str(datetime.now())
                })
                if serializer_consulta.is_valid():
                    serializer_consulta.save()
                    return Response(serializer_consulta.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            consulta = Consulta.objects.filter(ciudad=ciudad_obj.pk).first()
            
            fecha = datetime.strptime(consulta.hora_consulta, '%Y-%m-%d %H:%M:%S.%f')    
            minutos = (datetime.now() - fecha).seconds / 60
            if minutos >= 10:
                """Si pasan 10 minutos, vuelva a consumir la API"""
                temperatura = response['main']['temp']
                humedad = response['main']['humidity']
                velocidad_viento = response['wind']['speed']
                serializer_consulta = ConsultaSerializer(consulta, data = {
                    'ciudad': ciudad_obj.pk,
                    'temperatura': temperatura,
                    'humedad': humedad,
                    'velocidad_viento': velocidad_viento,
                    'hora_consulta': str(datetime.now())
                })
                if serializer_consulta.is_valid():
                    serializer_consulta.save()
                    return Response(serializer_consulta.data, status=status.HTTP_200_OK)
                
            else:
                """Sino traiga los datos que estaban"""
                serializer = ConsultaSerializer(consulta)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer_consulta.errors, status=status.HTTP_400_BAD_REQUEST)
                    
def get_consulta(url=None, ciudad=None):
    """Función para consumir api publica"""
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+ciudad+',co&appid=1508a9a4840a5574c822d70ca2132032'
    response = requests.get(url)
    return response.json()
    
