from django.contrib import admin

from .models import Feature, FeatureImage


@admin.register(FeatureImage)
class FeatureImageAdmin(admin.ModelAdmin):
    ...


class FeatureImageInline(admin.TabularInline):
    model = FeatureImage


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):

    inlines = [FeatureImageInline]



