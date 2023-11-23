from django.shortcuts import render
import requests


def home_page(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')
