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
    context = {
        'car_info' : pages_car,
        'info' : info,
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
    car_info = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            car_info = car_info.filter(description__icontains=keyword)
    context = {
        'car_info' : car_info,
    }
    return render(request,'cars/search.html',context)