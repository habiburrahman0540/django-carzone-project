from django.shortcuts import render
from pages.models import Team,TeamSection
from .models import About,ServiceSection ,Service,ServiceVideo
# Create your views here.
def aboutPage(request):
    about_data = About.objects.first()
    team_section = TeamSection.objects.first()
    teams = Team.objects.all()
    context = {
        'team_section':team_section,
        'teams' : teams,
        'about_data':about_data
    }
    return render(request,'pages/about.html',context)
def servicePage(request):
    service_section = ServiceSection.objects.first()
    services = Service.objects.order_by('created_date')
    service_video = ServiceVideo.objects.first()
    context = {
        'service_section' : service_section,
        'services':services,
        'service_video':service_video
    }
    return render(request,'pages/services.html',context)