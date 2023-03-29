from django.forms import ModelForm
from django import forms
from .models import Newborn, MotherDetails, MotherLocation, LabInvestigation, BirthRecord, Patient
from .models import SEROLOGY_CHOICES, MICROBIOLOGY_CHOICES, CHEMISTRY_CHOICES, HEMATOLOGY_CHOICES

class NewbornForm(ModelForm):
    class Meta:
        model = Newborn
        fields = ['name', 'sex', 'admission_date', 'date_of_birth', 'birth_weight', 'age_in_days', 'gestation_age', 'diagnosis']
        widgets = {
            'admission_date': forms.DateInput(
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
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'age_in_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'gestation_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MotherDetailForm(ModelForm):
    class Meta:
        model = MotherDetails
        fields = ['name', 'age', 'blood_group', 'parity', 'number_of_living_children', 'hiv_status', 'level_of_education', 'occupation']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_living_children': forms.NumberInput(attrs={'class': 'form-control'}),
            'parity': forms.TextInput(attrs={'class': 'form-control'}),
            'hiv_status': forms.Select(attrs={'class': 'form-control'}),
            'level_of_education': forms.Select(attrs={'class': 'form-control'}),
            'occupation': forms.Select(attrs={'class': 'form-control'}),
        }


class MotherLocationForm(ModelForm):
    class Meta:
        model = MotherLocation
        fields = ['country', 'district', 'subcounty', 'parish', 'village', 'contact', 'nin_no']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'subcounty': forms.TextInput(attrs={'class': 'form-control'}),
            'parish': forms.TextInput(attrs={'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'nin_no': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LabInvestigationForm(ModelForm):
    class Meta:
        model = LabInvestigation
        fields = ['serology', 'microbiology', 'chemistry', 'hematology']
        #widgets = {
         #       'serology': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
          #      'microbiology': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
           #     'chemistry': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            #    'hematology': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        #}



class BirthRecordForm(forms.ModelForm):
    class Meta:
        model = BirthRecord
        fields = ['place_of_birth', 'name_of_health_facility', 'location_of_health_facility', 'mode_of_delivery',
                  'indication_for_csection', 'time_btn_cs_and_delivery', 'resuscitation', 'length_of_resuscitation',
                  'was_ox_connected', 'referral', 'reason_for_referral', 'date_and_time_of_referral', 'mean_of_transport']
        widgets = {
            'place_of_birth': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
            'mode_of_delivery': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
            'resuscitation': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
            'referral': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
        }


class PatientForm(forms.ModelForm):
    symptoms = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)

    class Meta:
        model = Patient
        fields = [
            'symptoms',
            'general_findings',
            'respiratory_findings',
            'cardiovascular_findings',
            'abdominal_findings',
        ]
