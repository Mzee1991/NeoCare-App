from django.forms import ModelForm
from django import forms
from .models import Newborn, MotherDetails, MotherLocation, LabInvestigation
from .models import SEROLOGY_CHOICES, MICROBIOLOGY_CHOICES, CHEMISTRY_CHOICES, HEMATOLOGY_CHOICES

class NewbornForm(ModelForm):
    class Meta:
        model = Newborn
        fields = ['name', 'admission_date', 'date_of_birth', 'birth_weight', 'age_in_days', 'gestation_age', 'diagnosis', 'discharge_date']
        widgets = {
            'admission_date': forms.DateInput(
                format=['%d-%m-%Y'],
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'discharge_date': forms.DateInput(
                format=['%d-%m-%Y'],
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'date_of_birth': forms.DateInput(
                format=['%d-%m-%Y'],
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age_in_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'gestation_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MotherDetailForm(ModelForm):
    class Meta:
        model = MotherDetails
        fields = ['name', 'age', 'blood_group', 'parity', 'number_of_living_children', 'hiv_status', 'level_of_education', 'nin_no', 'occupation']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_living_children': forms.NumberInput(attrs={'class': 'form-control'}),
            'parity': forms.TextInput(attrs={'class': 'form-control'}),
            'hiv_status': forms.Select(attrs={'class': 'form-control'}),
            'level_of_education': forms.Select(attrs={'class': 'form-control'}),
            'nin_no': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.Select(attrs={'class': 'form-control'}),
        }


class MotherLocationForm(ModelForm):
    class Meta:
        model = MotherLocation
        fields = ['country', 'district', 'subcounty', 'parish', 'village', 'contact']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'subcounty': forms.TextInput(attrs={'class': 'form-control'}),
            'parish': forms.TextInput(attrs={'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class LabInvestigationForm(ModelForm):
    class Meta:
        model = LabInvestigation
        fields = ['serology', 'microbiology', 'chemistry', 'hematology']
        widgets = {
                'serology': forms.RadioSelect(attrs={'class': 'card-body card-body form-check'}),
                'microbiology': forms.RadioSelect(attrs={'class': 'form-check-input'}),
                'chemistry': forms.RadioSelect(attrs={'class': 'form-check-input'}),
                'hematology': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
