from .models import Calculates
from django import forms


class CalculatesForm(forms.ModelForm):
    class Meta:
        model = Calculates
        fields = ['x', 'y', 'sign']
