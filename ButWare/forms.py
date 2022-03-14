from django import forms
from .models import *

class AddEstimate(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = '__all__'
