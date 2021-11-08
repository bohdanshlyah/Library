from django.forms import ModelForm, SelectDateWidget
from datetime import datetime

from .models import Order


class UserOrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = ('book',)


class AdminOrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'end_at': SelectDateWidget()
        }
