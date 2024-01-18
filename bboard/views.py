from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .forms import IceCreamForm
from .models import IceCream, IceCreamKiosk, Comment, Task


def home_page(request):
    ice_creams = IceCream.objects.order_by('calories')
    ice_cream_kiosks = IceCreamKiosk.objects.all()
    context = {'ice_creams': ice_creams, 'ice_cream_kiosks': ice_cream_kiosks}
    return render(request, 'index.html', context)


def sms_view(request):
    messages = Comment.objects.all()
    return render(request, 'smsview.html', {'messages': messages})


def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "adminlogin" and password == "aabbddaa123":  # Сделать так, чтобы он искал в файле, если нету, то
            with open('txt_db/login', 'r+', encoding='utf-8') as file:  # Добавлял нового
                file.write(f'{username}={password}')
        else:
            return HttpResponseRedirect('about')

    return render(request, 'login.html')


class IceCreamDetailView(DetailView):
    model = IceCream

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['IceCream'] = IceCream.objects.all()
        return context


class IceCreamCreateView(CreateView):
    template_name = 'create.html'
    form_class = IceCreamForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['IceCream'] = IceCream.objects.all()
        return context

