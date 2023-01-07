from typing import ValuesView
from django import forms
from django.forms.widgets import NumberInput
from django.utils.regex_helper import Choice
from requests.models import to_key_val_list
from web.models import *
from django.forms import (
    IntegerField, DateTimeInput, TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField, FloatField
)
from datetime import date, datetime

class contactform(forms.ModelForm):

    Nombre = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'data-parsley-required': 'true',
    }), required=True)
