from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_title_extra = models.CharField(max_length=100)
    description = RichTextField()
    about_section_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    about_section_image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    about_section_image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    created_date = models.DateTimeField(auto_now_add = True,blank=True)
   
    def __str__(self):
        return self.about_title
    
class ServiceSection(models.Model):
    service_section_title = models.CharField(max_length=100)
    service_section_title_extra = models.CharField(max_length=100)
    service_section_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True,blank=True)
    
    def __str__(self):
        return self.service_section_title

class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=255)
    service_description = models.TextField()
    service_number = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add = True,blank=True)
    
    def __str__(self):
        return self.service_title

class ServiceVideo(models.Model):
    
    service_video_title = models.CharField(max_length=255)
    #service_video_title_extra = models.CharField(max_length=100)
    service_video_description = models.TextField()
    service_video_link = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add = True,blank=True)
    
    def __str__(self):
        return self.service_video_title