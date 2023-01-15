from django.contrib import admin

from .models import Location,GenreTag,Band,Event

admin.site.register(Location)
admin.site.register(GenreTag)
admin.site.register(Band)
admin.site.register(Event)
