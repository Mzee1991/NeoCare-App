from django.forms import ModelForm
from django import forms
from .models import Newborn
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'

class NewbornForm(ModelForm):
    class Meta:
        model = Newborn
        fields = ['name', 'admission_date', 'gestation_age', 'diagnosis', 'discharge_date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'admission_date': DateInput(),
            'gestation_age': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
            'discharge_date':DateInput()
        }
