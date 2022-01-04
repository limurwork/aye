from .models import EmployeeDetails
from django.forms import ModelForm, TextInput


class Detalis(ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['name', 'email', 'apartament']
        widgets = {
            'name':  TextInput(attrs={
                'class': 'from-control',
                'placeholder':'Имя'
            }),
            'email': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'мыло'
            }),
            'apartament': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'адрес'
            }),
        }