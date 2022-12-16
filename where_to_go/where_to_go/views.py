from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()

    places_list = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': reverse('show_place', args=[place.pk])
            }
        } for place in places]

    features = {
      'type': 'FeatureCollection',
      'features': places_list
    }

    context = {
        'features_json': features
    }

    return render(request, 'index.html', context)


def show_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = place.images.all()
    images_urls = [place_image.image.url for place_image in place_images]
    place_feature = model_to_dict(place)
    place_feature['imgs'] = images_urls

    return JsonResponse(
        place_feature,
        json_dumps_params={'ensure_ascii': False}
    )
