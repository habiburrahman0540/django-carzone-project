from django.urls import path
from . import views


urlpatterns=[
     path('about-us', views.aboutPage,name='about'),
     path('services', views.servicePage,name='services'),
]