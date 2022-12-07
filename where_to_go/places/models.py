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


class FeatureImage(models.Model):

    image = models.ImageField('Фото места', upload_to='palaces')
    alt = models.CharField('Alt изображения', max_length=150)
    feature = models.ForeignKey('Feature', on_delete=models.CASCADE, related_name='feature', blank=True, null=True)
    order = models.IntegerField('Позиция', default=1)

    class Meta:
        verbose_name = 'Фото места'
        verbose_name_plural = 'Фото мест'

    def __str__(self):
        return self.alt[:20]

