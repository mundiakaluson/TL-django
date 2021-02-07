from .models import Assign
from django import forms

class AssignForm(forms.Form):
    
    writer_assigned = forms.CharField(max_length=128)
    order_assigned = forms.CharField(max_length=128)