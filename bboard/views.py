from django.shortcuts import render
from .models import IceCream, IceCreamKiosk


def home_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def test_site(request):
    ice_creams = IceCream.objects.all()
    ice_cream_kiosks = IceCreamKiosk.objects.all()
    context = {'ice_creams': ice_creams}
    return render(request, 'testsite.html', context)
