from django.contrib import admin
from .models import links
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    list_display=['classname','link']

admin.site.register(links,LinkAdmin)