from django.shortcuts import render , get_object_or_404
from .models import Car
from pages.models import TopHeaderWithFooter
from django.core.paginator import Paginator
# Create your views here.
def cars(request):
    info = TopHeaderWithFooter.objects.get()
    car_info = Car.objects.order_by('-created_date')
    paginator = Paginator(car_info,1)
    page = request.GET.get('page')
    pages_car = paginator.get_page(page)
    #Search function
    search_model = Car.objects.values_list('model',flat=True).distinct()
    search_location = Car.objects.values_list('city',flat=True).distinct()
    search_year = Car.objects.values_list('year',flat=True).distinct()
    search_condition = Car.objects.values_list('condition',flat=True).distinct()
    search_body_style = Car.objects.values_list('body_style',flat=True).distinct()
    context = {
        'car_info' : pages_car,
        'info' : info,
        'search_model':search_model,
        'search_location':search_location,
        'search_year':search_year,
        'search_body_style':search_body_style,
        'search_condition':search_condition
    }
    return render(request, 'cars/cars.html',context)


def car_details(request,id):
    data = get_object_or_404(Car,pk=id)
    feature = data.features
    info = TopHeaderWithFooter.objects.get()
    context = {
        'data' : data,
        'feature' :feature,
        'info' : info,

    }
    return render(request,'cars/car_details.html',context)

def searchViews(request):
    search_model = Car.objects.values_list('model',flat=True).distinct()
    search_city = Car.objects.values_list('city',flat=True).distinct()
    search_year = Car.objects.values_list('year',flat=True).distinct()
    search_condition = Car.objects.values_list('condition',flat=True).distinct()
    search_transmission = Car.objects.values_list('transmission',flat=True).distinct()
    search_color = Car.objects.values_list('color',flat=True).distinct()
    car_info = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            car_info = car_info.filter(description__icontains=keyword)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            car_info = car_info.filter(model__iexact=model)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            car_info = car_info.filter(city__iexact=city)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            car_info = car_info.filter(year__iexact=year)
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            car_info = car_info.filter(body_style__iexact=body_style)
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            car_info = car_info.filter(transmission__iexact=transmission)
    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            car_info = car_info.filter(color__iexact=color)
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            car_info = car_info.filter(price__gte=min_price,price__lte=max_price)
    context = {
        'car_info' : car_info,
        'search_model':search_model,
        'search_city':search_city,
        'search_year':search_year,
        'search_condition':search_condition,
        'search_transmission':search_transmission,
        'search_color':search_color
    }
    return render(request,'cars/search.html',context)