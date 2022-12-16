import os
import urllib
from io import BytesIO
from urllib.parse import urlparse

import requests
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):

        response = requests.get(options['url'])
        response.raise_for_status()
        place = response.json()

        place = Place.objects.filter(title=place['title'])
        if not place:
            new_feature = Place.objects.create(
                title=place['title'],
                description_short=place['description_short'],
                description_long=place['description_long'],
                lng=place['coordinates']['lng'],
                lat=place['coordinates']['lat'],
            )
            for counter, img_url in enumerate(place['imgs']):
                response = requests.get(img_url)
                response.raise_for_status()

                file_path = urllib.parse.unquote(urlparse(img_url).path)
                path, file_name = os.path.split(file_path)

                image = BytesIO(response.content)
                place_image = Image.objects.create(
                    alt=place['title'][:20],
                    feature=new_feature,
                    order=counter
                )
                if place_image:
                    place_image.image.save(file_name, ImageFile(image))

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)
