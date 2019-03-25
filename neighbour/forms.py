from .models import *
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields=('name','neighbourhood','profile','email')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name'  , 'user' ,'neighbour' ,'email']

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields =['eventname','description','date']
