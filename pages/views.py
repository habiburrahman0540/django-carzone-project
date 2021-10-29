from django.shortcuts import render
from .models import Team,TopHeaderWithFooter
from cars.models import Car
# Create your views here.
def homePage(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    search_fields = Car.objects.values('model','city','year','body_style')
    context ={
        'teams':teams,
        'featured_cars' :featured_cars,
        'all_cars' : all_cars,
        'search_fields' : search_fields
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

