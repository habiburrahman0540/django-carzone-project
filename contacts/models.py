from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.email
class ContactSection(models.Model):
    contact_section_title = models.CharField(max_length=100)
    contact_section_title_extra = models.CharField(max_length=100)
    contact_section_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True,blank=True)
    
    def __str__(self):
        return self.contact_section_title
    
class ContactUs(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True,blank=True)
    
    def __str__(self):
        return self.subject