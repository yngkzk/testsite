from django.urls import path
from .views import home_page, sms_view, login_page, IceCreamCreateView, IceCreamDetailView

urlpatterns = [
    path('', home_page, name="index"),
    path('login/', login_page, name="login"),
    path('add/', IceCreamCreateView.as_view(), name="add"),
    path('detail/<int:pk>/', IceCreamDetailView.as_view(), name="detail"),
    path('smsview/', sms_view, name="smsview"),
]
