
from django import forms

from web.models import *
from django.forms import (
    IntegerField, DateTimeInput, TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField, FloatField
)


class contactform(forms.ModelForm):

    nombre = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'data-parsley-required': 'true',
    }), required=True)

    correo = forms.EmailField(widget=TextInput(attrs={
        'class': 'form-control',
        'type':'email',
        'data-parsley-required': 'true',
    }), required=True)

    asunto = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'data-parsley-required': 'true',
    }), required=True)

    mensaje = forms.CharField(widget=Textarea(attrs={
        'rows': '5',
        'class': 'form-control',
        'data-parsley-required': 'true',
    }), required=True)

    class Meta:
        model = contact
        fields = [
            'nombre',
            'correo',
            'asunto',
            'mensaje',

        ]

