from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


@admin.register(Image)
class FeatureImageAdmin(admin.ModelAdmin):
    pass


class FeatureImageInline(SortableTabularInline):
    model = Image

    list_display = ('order', 'image', 'place')

    readonly_fields = ('image_tag',)

    extra = 1

    def image_tag(self, obj):
        fixed_width = 200
        width_percent = (fixed_width / float(obj.image.width))
        height_size = int((float(obj.image.height) * float(width_percent)))
        return mark_safe(f'<img src="{obj.image.url}" width="{fixed_width}" height={height_size} />')


@admin.register(Place)
class FeatureAdmin(SortableAdminBase, admin.ModelAdmin):

    list_display = ('title', )

    inlines = [FeatureImageInline]



