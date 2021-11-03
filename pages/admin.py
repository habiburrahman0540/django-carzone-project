from django.contrib import admin
from .models import TeamSection,Team,TopHeaderWithFooter
from cars.models import FeaturedCarSection ,LatestCarSection
from django.utils.html import format_html
# Register your models here.
admin.site.site_header = 'Carzone Admin panel'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Carzone'
@admin.register(FeaturedCarSection)
class AdminFeaturedCarSection(admin.ModelAdmin):
    list_display = ('featured_car_section_title','featured_car_section_title_extra','featured_car_section_description')
    list_display_links =('featured_car_section_title',)
  
    def has_add_permission(self, request):
        save_as_continue = False
        show_save_and_add_another = False
        extra_context  = False
        save_as = False
        data = FeaturedCarSection.objects.all()
        if data:
            return False
        return True
   
@admin.register(LatestCarSection)
class AdminLatestCarSection(admin.ModelAdmin):
    list_display = ('Latest_car_section_title','Latest_car_section_title_extra','Latest_car_section_description')
    list_display_links =('Latest_car_section_title',)
  
    def has_add_permission(self, request):
        save_as_continue = False
        show_save_and_add_another = False
        extra_context  = False
        save_as = False
        data = LatestCarSection.objects.all()
        if data:
            return False
        return True
   
@admin.register(TeamSection)
class AdminTeamSection(admin.ModelAdmin):
    list_display = ('Team_section_title','Team_section_title_extra','Team_section_description')
    list_display_links =('Team_section_title',)
  
    def has_add_permission(self, request):
        save_as_continue = False
        show_save_and_add_another = False
        extra_context  = False
        save_as = False
        data = TeamSection.objects.all()
        if data:
            return False
        return True
    
@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('first_name','last_name','thumbnail','designation','created_date')
    list_display_links=('first_name','last_name','designation','thumbnail')
    list_per_page = 10
    list_filter =('designation',)
    search_fields =('first_name','last_name','designation')

@admin.register(TopHeaderWithFooter)
class AdminTopHeaderAndFooter(admin.ModelAdmin):
    list_display =('phone','email','workingday_start','workingday_end','Time_start','Time_end','footer_text')