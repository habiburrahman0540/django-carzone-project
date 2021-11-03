from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
      list_display =('id','first_name','last_name','email','car_title','message')
      list_display_links = ('first_name','last_name')
      search_fields =('first_name','last_name')
      list_per_page = 10