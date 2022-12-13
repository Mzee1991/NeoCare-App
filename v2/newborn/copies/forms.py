from django.forms import ModelForm
from django import forms
from .models import Newborn
from bootstrap_datepicker_plus.widgets import DatePickerInput


class NewbornForm(ModelForm):
    class Meta:
        model = Newborn
        fields = ['name', 'admission_date', 'gestation_age', 'diagnosis', 'discharge_date']

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'admission_date': DatePickerInput(options={"format": "DD-MM-YYYY"}),
        'gestation_age': forms.TextInput(attrs={'class': 'form-control'}),
        'diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
        'discharge_date': DatePickerInput(options={"format": "DD-MM-YYYY"})
    }

