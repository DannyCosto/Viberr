from django.contrib import admin
from .models import Album, Song
# imports albums to admin page
admin.site.register(Album)
admin.site.register(Song)