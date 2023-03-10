from django.db import models
from main.models.room import Room


# Modelo Articulo
class Article(models.Model):
    name_article = models.CharField('Nombre del artículo', max_length=32, default='')
    description_article = models.TextField('Descripción del artículo')
    value = models.FloatField('Valor')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, verbose_name='Salon', null=True, blank=True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return "Articulo " + self.pk
