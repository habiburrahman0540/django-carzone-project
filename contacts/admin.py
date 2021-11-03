from django.contrib import admin
from .models import Contact,ContactUs,ContactSection
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
      list_display =('id','first_name','last_name','email','car_title','message')
      list_display_links = ('first_name','last_name')
      search_fields =('first_name','last_name')
      list_per_page = 10
      
@admin.register(ContactSection)
class AdminContactSection(admin.ModelAdmin):
    list_display = ('contact_section_title','contact_section_title_extra','contact_section_description')
    list_display_links =('contact_section_title',)
  
    def has_add_permission(self, request):
        save_as_continue = False
        show_save_and_add_another = False
        extra_context  = False
        save_as = False
        data = ContactSection.objects.all()
        if data:
            return False
        return True
      
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
      list_display = ('full_name','email','phone','subject','message')
      list_per_page = 10
      search_fields = ('created_date','email','phone','full_name')