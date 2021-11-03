from django.shortcuts import render
from .models import Team,TopHeaderWithFooter
from cars.models import Car,FeaturedCarSection,LatestCarSection
# Create your views here.
def homePage(request):
    teams = Team.objects.all()
    FeaturedCarSections = FeaturedCarSection.objects.first()
    LatestCarSections = LatestCarSection.objects.first()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    search_model = Car.objects.values_list('model',flat=True).distinct()
    search_location = Car.objects.values_list('city',flat=True).distinct()
    search_year = Car.objects.values_list('year',flat=True).distinct()
    search_body_style = Car.objects.values_list('body_style',flat=True).distinct()
    context ={
        'FeaturedCarSections': FeaturedCarSections,
        'LatestCarSections':LatestCarSections,
        'teams':teams,
        'featured_cars' :featured_cars,
        'all_cars' : all_cars,
        'search_model':search_model,
        'search_location':search_location,
        'search_year':search_year,
        'search_body_style' : search_body_style
        }
    return render(request,'pages/home.html',context)



def carPage(request):
    return render(request,'pages/cars.html')


