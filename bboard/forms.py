from django.forms import ModelForm
from .models import IceCreamKiosk


class IceCreamKioskForm(ModelForm):
    class Meta:
        model = IceCreamKiosk
        fields = ('flavor', 'price', 'portion_size', 'ingredients', 'calories')
