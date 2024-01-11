from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import IceCream, IceCreamKiosk, Comment


def home_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def test_site(request):
    ice_creams = IceCream.objects.order_by('calories')
    ice_cream_kiosks = IceCreamKiosk.objects.all()
    context = {'ice_creams': ice_creams, 'ice_cream_kiosks': ice_cream_kiosks}
    return render(request, 'testsite.html', context)


def sms_view(request):
    messages = Comment.objects.all()
    return render(request, 'smsview.html', {'messages': messages})


def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "adminlogin" and password == "aabbddaa123":
            pass
        else:
            return HttpResponseRedirect('about')

    return render(request, 'login.html')
