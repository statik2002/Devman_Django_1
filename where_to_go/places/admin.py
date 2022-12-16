from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class ImageInline(SortableTabularInline):
    model = Image
    list_display = ('order', 'image', 'place')
    readonly_fields = ('get_image_thumbnail',)
    extra = 1

    def get_image_thumbnail(self, obj):
        return mark_safe(
            f'<img style="max-height: 200px" src="{obj.image.url}" />'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )
    inlines = [ImageInline]
