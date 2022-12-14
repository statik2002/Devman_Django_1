from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Place, Image


def show_phones(request):

    places = Place.objects.prefetch_related('images').all()

    places_list = []
    for place in places:
        feature_params = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
                "detailsUrl": reverse('show_place', args=[place.pk])
            }
        }
        places_list.append(feature_params)

    features_json = {
      "type": "FeatureCollection",
      "features": places_list
    }

    context = {
        'features_json': features_json
    }

    return render(request, 'index.html', context)


def show_place(request, place_id):

    place = get_object_or_404(Place, pk=place_id)
    place_images = Image.objects.filter(feature=place)

    images_urls = []
    for place_image in place_images:
        images_urls.append(place_image.image.url)

    place_dict = model_to_dict(place)

    place_dict['imgs'] = images_urls

    return JsonResponse(place_dict, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
