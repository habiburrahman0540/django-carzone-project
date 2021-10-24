from django.shortcuts import render
from .models import Team
# Create your views here.
def homePage(request):
    teams = Team.objects.all()
    data ={
        'teams':teams
    }
    return render(request,'pages/home.html',data)

def aboutPage(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams
    }
    return render(request,'pages/about.html',data)

def servicePage(request):
    return render(request,'pages/services.html')
def carPage(request):
    return render(request,'pages/cars.html')
def contactPage(request):
    return render(request,'pages/contact.html')
