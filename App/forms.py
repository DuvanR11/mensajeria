from django import forms
from App.models import *

class Costumerform(forms.ModelForm):
    file = forms.FileField(required=False)
    estado = forms.CharField(required=False) 
    class Meta:
        model = Costumer
        fields = '__all__'
        
