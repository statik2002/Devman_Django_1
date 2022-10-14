from django.contrib import admin

from .models import Feature


class FeatureAdmin(admin.ModelAdmin):
    ...


admin.site.register(Feature, FeatureAdmin)
