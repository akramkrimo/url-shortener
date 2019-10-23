from django.contrib import admin
from .models import UrlShortcut
# Register your models here.

class UrlAdmin(admin.ModelAdmin):

    fields = ['raw_url', 'short_url']
    list_display = ('short_url', 'creation_date')


admin.site.register(UrlShortcut, UrlAdmin)