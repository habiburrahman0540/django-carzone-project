from django.contrib import admin
from .models import About,ServiceSection,Service,ServiceVideo
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','about_title')
    list_display_links =('about_title',)
  
    def has_add_permission(self, request):
        save_as_continue = False
        show_save_and_add_another = False
        extra_context  = False
        save_as = False
        data = About.objects.all()
        if data:
            return False
        return True

@admin.register(ServiceSection)
class AdminServiceSection(admin.ModelAdmin):
    list_display = ('id','service_section_title','service_section_title_extra','service_section_description')
    list_display_links =('service_section_title',)
  
    def has_add_permission(self, request):
        save_as_continue = False
        show_save_and_add_another = False
        extra_context  = False
        save_as = False
        data = ServiceSection.objects.all()
        if data:
            return False
        return True

@admin.register(Service)
class AdminServiceSection(admin.ModelAdmin):
    list_display = ('id','service_icon','service_title','service_number','service_description')
    list_display_links =('service_title',)
    

@admin.register(ServiceVideo)
class AdminServiceSection(admin.ModelAdmin):
    list_display = ('id','service_video_title','service_video_description','service_video_link')
    list_display_links =('service_video_title',)
  
    def has_add_permission(self, request):
        save_as_continue = False
        show_save_and_add_another = False
        extra_context  = False
        save_as = False
        data = ServiceVideo.objects.all()
        if data:
            return False
        return True