from django.contrib import admin
from gallery.models import Gallery
from pages.models import  Page

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Page)