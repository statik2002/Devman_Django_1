# Generated by Django 3.2.15 on 2022-12-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_featureimage_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureimage',
            name='image',
            field=models.ImageField(upload_to='palaces', verbose_name='Фото места'),
        ),
    ]
