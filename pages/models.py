from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    linkedIn_link = models.URLField(max_length=100,blank=True)
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.first_name


class TopHeaderWithFooter(models.Model):
    phone = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=254,unique=True)
    workingday_start = models.CharField(max_length=100,blank=True)
    workingday_end = models.CharField(max_length=100,blank=True)
    Time_start = models.PositiveIntegerField(default=0,blank=True)    
    Time_end = models.PositiveIntegerField(default=0,blank=True)
    footer_text = models.CharField(max_length=255)
    developed_by = models.CharField(max_length=255,blank=True)
    facebook_link = models.URLField(max_length=100,blank=True)
    twitter_link = models.URLField(max_length=100,blank=True)
    google_plus_link = models.URLField(max_length=100,blank=True)
    linkedIn_link = models.URLField(max_length=100,blank=True)
    created_date = models.DateTimeField(auto_now_add = True,blank=True)
        