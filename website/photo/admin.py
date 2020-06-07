from django.contrib import admin
from photo.models import Album, Photo
# Register your models here.

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    inlines = (PhotoInline,)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')