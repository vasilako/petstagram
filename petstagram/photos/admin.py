from django.contrib import admin

from petstagram.photos.models import Photos


# Register your models here.
@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['photo']