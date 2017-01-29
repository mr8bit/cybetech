from django.forms import ModelForm

from .models import *


# Create the form class.
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'name', 'name_company', 'massage', 'phone']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['email', 'name', 'name_company', 'massage', 'order', 'phone']
