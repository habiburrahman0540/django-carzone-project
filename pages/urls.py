from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage,name='home'),
    path('about-us', views.aboutPage,name='about'),
    path('services', views.servicePage,name='services'),
    path('contact-us', views.contactPage,name='contact'),
]
