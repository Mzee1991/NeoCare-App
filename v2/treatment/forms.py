from django.forms import ModelForm
from django import forms
from treatment.models import Prescription

class PrescriptionForm(forms.ModelForm):
    start_dose_time = forms.TimeField(required=False, label='Start Dose Time')
    second_dose_time = forms.TimeField(required=False, label='Second Dose Time')
    third_dose_time = forms.TimeField(required=False, label='Third Dose Time')
    fourth_dose_time = forms.TimeField(required=False, label='Fourth Dose Time')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            self.fields['prescriber'].initial = user

    class Meta:
        model = Prescription
        fields = ['name', 'start_dose_time', 'second_dose_time', 'third_dose_time', 'fourth_dose_time', 'frequency', 'prescriber']
