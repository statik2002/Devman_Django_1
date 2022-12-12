# Generated by Django 4.1.4 on 2022-12-12 07:54

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_feature_options_alter_featureimage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='feature',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description_short',
            field=tinymce.models.HTMLField(),
        ),
    ]