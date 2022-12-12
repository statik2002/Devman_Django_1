import json
from pprint import pprint

from django.core import serializers
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Feature, FeatureImage


def show_phones(request):

    features = Feature.objects.prefetch_related('images').all()

    features_list = []
    for feature in features:
        feature_params = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [feature.lng, feature.lat]
            },
            "properties": {
                "title": feature.title,
                "placeId": "moscow_legends",
                "detailsUrl": reverse('show_place', args=[feature.pk])
            }
        }
        features_list.append(feature_params)

    features_json = {
      "type": "FeatureCollection",
      "features": features_list
    }

    context = {
        'features_json': features_json
    }

    return render(request, 'index.html', context)


def show_place(request, place_id):

    place = get_object_or_404(Feature, pk=place_id)
    place_images = FeatureImage.objects.filter(feature=place)

    images_urls = []
    for place_image in place_images:
        images_urls.append(place_image.image.url)

    place_dict = model_to_dict(place)

    place_dict['imgs'] = images_urls

    return JsonResponse(place_dict, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
