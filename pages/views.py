from django.shortcuts import render
from .models import Team,TopHeaderWithFooter
from cars.models import Car
# Create your views here.
def homePage(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    search_model = Car.objects.values_list('model',flat=True).distinct()
    search_location = Car.objects.values_list('city',flat=True).distinct()
    search_year = Car.objects.values_list('year',flat=True).distinct()
    search_body_style = Car.objects.values_list('body_style',flat=True).distinct()
    context ={
        'teams':teams,
        'featured_cars' :featured_cars,
        'all_cars' : all_cars,
        'search_model':search_model,
        'search_location':search_location,
        'search_year':search_year,
        'search_body_style' : search_body_style
        }
    return render(request,'pages/home.html',context)

def aboutPage(request):
    teams = Team.objects.all()
    context = {
        'teams' : teams,
    }
    return render(request,'pages/about.html',context)

def servicePage(request):
    return render(request,'pages/services.html')
def carPage(request):
    return render(request,'pages/cars.html')
def contactPage(request):
    return render(request,'pages/contact.html')

