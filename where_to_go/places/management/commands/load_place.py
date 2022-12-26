import os
import urllib
from io import BytesIO
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


def upload_image(images_urls, place):
    for counter, img_url in enumerate(images_urls):
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


class Command(BaseCommand):
    help = 'Скрипт загрузки данных из JSON файла.'

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_payload = response.json()

        place, created = Place.objects.update_or_create(
            title=place_payload['title'],
            lng=place_payload['coordinates']['lng'],
            lat=place_payload['coordinates']['lat'],
            defaults={
                'description_short': place_payload.get('description_short', ''),
                'description_long': place_payload.get('description_long', ''),
            }
        )

        upload_image(place_payload.get('imgs', []), place)

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)
