from django.urls import path
from .views import home_page, contact_page, about_page, test_site, sms_view

urlpatterns = [
    path('', home_page, name="index"),
    path('about', about_page, name="about"),
    path('home', home_page, name="home"),
    path('contacts', contact_page, name="contacts"),
    path('testsite', test_site, name="testsite"),
    path('smsview', sms_view, name="smsview"),
]
