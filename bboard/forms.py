from django.forms import ModelForm
from .models import IceCreamKiosk, IceCream


class IceCreamKioskForm(ModelForm):
    class Meta:
        model = IceCreamKiosk
        fields = ('location', 'prices', 'working_hours', 'staff_info', 'special_offers')


class IceCreamForm(ModelForm):
    class Meta:
        model = IceCream
        fields = ('flavor', 'price', 'portion_size', 'ingredients', 'calories')

