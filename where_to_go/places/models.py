from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class Place(models.Model):

    title = models.CharField('Заголовок', max_length=250)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)
    lng = models.FloatField('Широта', default=0.0)
    lat = models.FloatField('Долгота', default=0.0)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feature-detail', kwargs={'pk': self.pk})


class Image(models.Model):

    image = models.ImageField('Фото места', upload_to='palaces')
    alt = models.CharField('Alt изображения', max_length=150)
    feature = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    order = models.IntegerField('Позиция', default=1)

    class Meta:
        verbose_name = 'Фото места'
        verbose_name_plural = 'Фото мест'
        ordering = ['order']

    def __str__(self):
        return self.alt[:20]

