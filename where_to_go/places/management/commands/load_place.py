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
        place_payload = response.json()

        if not place_payload.get('coordinates').get('lng') \
                or not place_payload.get('coordinates').get('lat'):
            return

        place, created = Place.objects.update_or_create(
            title=place_payload.get('title', 'Без названия'),
            defaults={
                'description_short': place_payload.get('description_short', ''),
                'description_long': place_payload.get('description_long', ''),
                'lng': place_payload.get('coordinates').get('lng'),
                'lat': place_payload.get('coordinates').get('lat')
            }
        )

        for counter, img_url in enumerate(place_payload.get('imgs', [])):
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
