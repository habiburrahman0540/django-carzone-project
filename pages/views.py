from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request,'pages/home.html')
def aboutPage(request):
    return render(request,'pages/about.html')
def servicePage(request):
    return render(request,'pages/services.html')
def carPage(request):
    return render(request,'pages/cars.html')
def contactPage(request):
    return render(request,'pages/contact.html')
