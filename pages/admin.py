from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
admin.site.site_header = 'Carzone Admin panel'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Carzone'

class AdminTeam(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('first_name','last_name','thumbnail','designation','created_date')
    list_display_links=('first_name','last_name','designation','thumbnail')
    list_per_page = 10
    list_filter =('designation',)
    search_fields =('first_name','last_name','designation')
    
admin.site.register(Team,AdminTeam)