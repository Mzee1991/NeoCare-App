from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import LabRequest, LabResult


class LabTestRequestForm(ModelForm):
    class Meta:
        model = LabRequest
        fields = [
            'serology_rpr_requested',
            'serology_rct_requested',
            'serology_bat_requested',
            'microbiology_gram_stain_requested',
            'microbiology_culture_requested',
            'chemistry_serum_electrolytes_requested',
            'chemistry_serum_urea_requested',
            'chemistry_serum_creatinine_requested',
            'chemistry_urinalysis_requested',
        ]


class LabResultForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Get the lab_request instance passed as a keyword argument
        lab_request = kwargs.pop('lab_request', None)
        super().__init__(*args, **kwargs)

        # Get the requested tests from the lab_request
        requested_tests = []
        if lab_request:
            requested_tests.extend([
                'serology_rpr_result',
                'serology_rct_result',
                'serology_bat_result',
                'microbiology_gram_stain_result',
                'microbiology_culture_result',
                'chemistry_serum_electrolytes_result',
                'chemistry_serum_urea_result',
                'chemistry_serum_creatinine_result',
                'chemistry_urinalysis_result',
            ])
            # Remove fields that were not requested
            for field in self.fields.copy():
                if field not in requested_tests:
                    del self.fields[field]

            # Add form-control class to input fields
            for field_name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = LabResult
        fields = [
            'serology_rpr_result',
            'serology_rct_result',
            'serology_bat_result',
            'microbiology_gram_stain_result',
            'microbiology_culture_result',
            'chemistry_serum_electrolytes_result',
            'chemistry_serum_urea_result',
            'chemistry_serum_creatinine_result',
            'chemistry_urinalysis_result',
        ]

class DynamicLabResultForm(LabResultForm):
    def __init__(self, *args, test_name=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove all fields from the form
        self.fields.clear()

        # Determine which fields to include based on the selected test_name
        if test_name == 'serology_rpr':
            self.fields['serology_rpr_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='RPR Result')
        elif test_name == 'serology_rct':
            self.fields['serology_rct_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='RCT Result')
        elif test_name == 'serology_bat':
            self.fields['serology_bat_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='BAT Result')
        elif test_name == 'microbiology_gram_stain':
            self.fields['microbiology_gram_stain_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Gram stain Result')
        elif test_name == 'microbiology_culture':
            self.fields['microbiology_culture_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Culture Result')
        elif test_name == 'chemistry_serum_electrolytes':
            self.fields['chemistry_serum_electrolytes_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Serum Electrolytes')
        elif test_name == 'chemistry_serum_urea':
            self.fields['chemistry_serum_urea_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Serum Urea')
        elif test_name == 'chemistry_serum_creatinine':
            self.fields['chemistry_serum_creatinine_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        elif test_name == 'chemistry_urinalysis':
            self.fields['chemistry_urinalysis_result'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
