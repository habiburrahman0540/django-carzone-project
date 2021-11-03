from pages.models import TopHeaderWithFooter

def Topheader(request):
    data = TopHeaderWithFooter.objects.first()
    return {'data':data}