#Django
from django.db import models


class Ciudad(models.Model):
    """Modelo Ciudad"""
    nombre = models.CharField("Nombre de ciudad", max_length=50, blank=False, null=False, unique=True)
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.nombre


class Consulta(models.Model):
    """Modelo Consulta"""
    ciudad = models.ForeignKey(Ciudad, verbose_name="Ciudad", on_delete=models.CASCADE)
    hora_consulta = models.DateTimeField("Hora de consulta", auto_now=False, auto_now_add=True)
    temperatura = models.FloatField("Temperatura ciudad", blank=False, null=False)
    humedad = models.PositiveIntegerField("Humedad de ciudad", blank=False, null=False)
    velocidad_viento = models.FloatField("Velocidad del viento", blank=False, null=False)
    
    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return str(self.pk)+' '+self.ciudad.nombre