from datetime import datetime
from re import sub
from django.shortcuts import render
from .models import Contact, Package,Hotel

# Create your views here.
def index(req):
    return render(req,'travel/index.html')

def about(req):
    return render(req,'travel/about.html')

def packages(req):
    packages = Package.objects.all()
    return render(req,'travel/packages.html',{'packages':packages})

def hotels(req):
    allhotels = Hotel.objects.all()
    return render(req,'travel/hotels.html',{'hotels':allhotels})

def contact(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        subject = req.POST.get('subject')
        message = req.POST.get('message')
        print(name,email,subject,message)

        contact = Contact(name=name,email=email,subject=subject,message=message,date=datetime.now())
        contact.save()
        

        
    return render(req,'travel/contact.html')

