from django.urls import path
from .views import home_page, sms_view, login_page, IceCreamCreateView

urlpatterns = [
    path('', home_page, name="index"),
    path('login/', login_page, name="login"),
    path('add/', IceCreamCreateView.as_view(), name="add"),
    path('smsview/', sms_view, name="smsview"),
]
