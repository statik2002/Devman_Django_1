# Generated by Django 4.1.4 on 2022-12-14 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_alter_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True),
        ),
    ]
