from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)
    lng = models.FloatField('Широта')
    lat = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Фото места', upload_to='palaces')
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images',
        blank=True,
        null=True
    )
    order = models.IntegerField('Позиция', default=1)

    class Meta:
        verbose_name = 'Фото места'
        verbose_name_plural = 'Фото мест'
        ordering = ['order']

    def __str__(self):
        return f'{self.image.name} --- {self.place.title[:10]}'
