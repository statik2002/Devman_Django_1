from django.db import models
from django.urls import reverse


class Feature(models.Model):

    title = models.CharField('Заголовок', max_length=250)
    description_short = models.CharField('Короткое описание', max_length=250)
    description_long = models.TextField('Полное описание')
    lng = models.FloatField('Широта', default=0.0)
    lat = models.FloatField('Долгота', default=0.0)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feature-detail', kwargs={'pk': self.pk})



