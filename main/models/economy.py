from django.db import models
from main.models.tutor import Tutor


# Modelo Economia, datos economicos
class Economy(models.Model):
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    son = models.IntegerField('Número de hijos en el circulo')  # Numero de hijos en el circulo
    members = models.IntegerField('Número de miembros del nucleo familiar')  # Numero de miembros del nucleo familiar

    class Meta:
        verbose_name = 'Dato Económico'
        verbose_name_plural = 'Datos Económicos'

    def __str__(self):
        return 'Datos economicos de {}'.format(self.tutor.name_tutor)
