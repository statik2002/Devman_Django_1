import os
import urllib
from io import BytesIO
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Скрипт загрузки данных из JSON файла.'

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_from_file = response.json()

        place, created = Place.objects.update_or_create(
            title=place_from_file.get('title'),
            description_short=place_from_file.get('description_short', ''),
            description_long=place_from_file.get('description_long', ''),
            lng=place_from_file.get('coordinates').get('lng'),
            lat=place_from_file.get('coordinates').get('lat'),
            defaults={'title': place_from_file.get('title')}
        )

        if not created:
            return

        for counter, img_url in enumerate(place_from_file.get('imgs', [])):
            response = requests.get(img_url)
            response.raise_for_status()

            file_path = urllib.parse.unquote(urlparse(img_url).path)
            path, file_name = os.path.split(file_path)

            image = BytesIO(response.content)
            Image.objects.create(
                place=place,
                order=counter,
                image=ContentFile(image.read(), name=file_name)
            )

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)
