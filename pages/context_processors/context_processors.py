from pages.models import TopHeaderWithFooter

def Topheader(request):
    data = TopHeaderWithFooter.objects.get()
    return {'data':data}