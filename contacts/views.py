from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def contactPage(request):
    return render(request,'pages/contact.html')
def inquery(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_title = request.POST['car_title']
        car_id = request.POST['car_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contracted = Contact.objects.all().filter(user_id=user_id,car_id=car_id)
            if has_contracted:
                messages.error(request,"Yo have already inquery about this car , please wait until we get back to you.")
                return redirect('/cars/'+ car_id)
            
        contact = Contact(user_id=user_id,car_title=car_title,car_id=car_id,first_name=first_name,last_name=last_name,customer_need=customer_need,city=city, state=state,email=email,phone=phone,message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
        'You received a new inquery -'+ car_title,
        'Dear Admin, your received a new inquery from '+first_name+'.please login to your admin panel to read more.',
        'habiburrahman054@gmail.com',
        [admin_email],
        fail_silently=False,)
        contact.save()
        messages.success(request,'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+ car_id)