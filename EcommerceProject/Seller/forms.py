from django import forms
from .models import Laptop, Mobile, Grocery

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'

class MobileModelForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

class GroceryModelForm(forms.ModelForm):
    class Meta:
        model=Grocery
        fields='__all__'
