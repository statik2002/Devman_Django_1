from pprint import pprint

from django.shortcuts import render
from django.db.models import Prefetch
from places.models import Feature, FeatureImage


def show_phones(request):

    features = Feature.objects.prefetch_related('images').all()

    features_json = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "places/static/places/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "places/static/places/roofs24.json"
          }
        }
      ]
    }

    context = {
        'features_json': features_json
    }

    return render(request, 'index.html', context)
