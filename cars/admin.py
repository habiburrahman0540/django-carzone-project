from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.car_photo.url))
    thumbnail.short_description = 'Car Image'
    list_display = ('thumbnail','car_title','model','year','condition','price','is_featured')
    list_editable = ('is_featured',)
    list_display_link = ('car_title','model')
    search_fields = ('car_title','model','year','condition','price')
    list_filter = ('model','condition')
    list_per_page = 10