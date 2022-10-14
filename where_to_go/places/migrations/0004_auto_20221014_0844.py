# Generated by Django 3.0 on 2022-10-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20221014_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='lat',
            field=models.FloatField(default=0.0, verbose_name='Долгота'),
        ),
        migrations.AddField(
            model_name='feature',
            name='lng',
            field=models.FloatField(default=0.0, verbose_name='Широта'),
        ),
        migrations.DeleteModel(
            name='Coordinates',
        ),
    ]
