from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Feature, FeatureImage


@admin.register(FeatureImage)
class FeatureImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'order')
    ordering = ('order', )


class FeatureImageInline(admin.TabularInline):
    model = FeatureImage

    readonly_fields = ('image_tag',)

    extra = 1

    def image_tag(self, obj):
        fixed_width = 200
        width_percent = (fixed_width / float(obj.image.width))
        height_size = int((float(obj.image.height) * float(width_percent)))
        return mark_safe(f'<img src="{obj.image.url}" width="{fixed_width}" height={height_size} />')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):

    inlines = [FeatureImageInline]



