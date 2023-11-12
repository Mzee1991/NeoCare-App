from django import forms
from .models import Registration, Measurements, LabRequestChildren, LabResultChildren

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['location', 'registered_by']  # Exclude fields with foreign keys
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}))

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'second_name': forms.TextInput(attrs={'class': 'form-control'}),
        'other_names': forms.TextInput(attrs={'class': 'form-control'}),
        ##'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'autocomplete': 'off'}),
        'sex': forms.Select(attrs={'class': 'form-control'}),
        'religion': forms.Select(attrs={'class': 'form-control'}),
        'tribe': forms.TextInput(attrs={'class': 'form-control'}),
        'next_of_kin': forms.TextInput(attrs={'class': 'form-control'}),
        'relationship': forms.Select(attrs={'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        # Customize select fields with an empty option
        empty_option = [('', 'Select')]
        self.fields['sex'].choices = empty_option + list(self.fields['sex'].choices)
        self.fields['religion'].choices = empty_option + list(self.fields['religion'].choices)
        self.fields['relationship'].choices = empty_option + list(self.fields['relationship'].choices)


class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ['weight', 'height', 'blood_pressure', 'temperature', 'head_circumference', 'respiration', 'pulse', 'muac', 'oxygen']


class LabRequestChildrenForm(forms.ModelForm):
    class Meta:
        model = LabRequestChildren
        fields = [
            'serum_electrolytes_requested',
            'serum_bilirubin_requested',
            'serum_ast_requested',
            'serum_alt_requested',
            'serum_alp_requested',
            'serum_urea_requested',
            'serum_creatinine_requested',
            'complete_blood_count_requested',
            'blood_grouping_requested',
            'peripheral_thin_film_requested',
            'blood_smear_requested',
            'urinalysis_requested',
            'stool_analysis_requested',
            'h_pylori_stool_antigen_test_requested',
            'antistreptolysin_test_requested',
            'hepatitis_b_surface_antigen_requested',
            'malaria_rdts_requested',
            'rbs_requested',
            'rct_requested',
            'rpr_requested',
            'sickling_test_requested',
        ]


from django.forms import ModelForm, CharField, TextInput
from django import forms
from .models import LabResultChildren

class LabResultChildrenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # Get the lab_request instance passed as a keyword argument
        lab_request = kwargs.pop('lab_request', None)
        super().__init__(*args, **kwargs)

        # Get the requested tests from the lab_request
        requested_tests = []
        if lab_request:
            requested_tests.extend([
                'serum_electrolytes_result',
                'serum_bilirubin_result',
                'serum_ast_result',
                'serum_alt_result',
                'serum_alp_result',
                'serum_urea_result',
                'serum_creatinine_result',
                'complete_blood_count_result',
                'blood_grouping_result',
                'peripheral_thin_film_result',
                'blood_smear_result',
                'urinalysis_result',
                'stool_analysis_result',
                'h_pylori_stool_antigen_test_result',
                'antistreptolysin_test_result',
                'hepatitis_b_surface_antigen_result',
                'malaria_rdts_result',
                'rbs_result',
                'rct_result',
                'rpr_result',
                'sickling_test_result',
            ])
            # Remove fields that were not requested
            for field in self.fields.copy():
                if field not in requested_tests:
                    del self.fields[field]

            # Add form-control class to input fields
            for field_name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = LabResultChildren
        fields = [
            'serum_electrolytes_result',
            'serum_bilirubin_result',
            'serum_ast_result',
            'serum_alt_result',
            'serum_alp_result',
            'serum_urea_result',
            'serum_creatinine_result',
            'complete_blood_count_result',
            'blood_grouping_result',
            'peripheral_thin_film_result',
            'blood_smear_result',
            'urinalysis_result',
            'stool_analysis_result',
            'h_pylori_stool_antigen_test_result',
            'antistreptolysin_test_result',
            'hepatitis_b_surface_antigen_result',
            'malaria_rdts_result',
            'rbs_result',
            'rct_result',
            'rpr_result',
            'sickling_test_result',
        ]

class DynamicLabResultChildrenForm(LabResultChildrenForm):
    def __init__(self, *args, test_name=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove all fields from the form
        self.fields.clear()

        # Determine which fields to include based on the selected test_name
        if test_name == 'serum_electrolytes':
            self.fields['serum_electrolytes_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Serum Electrolytes Result')
        elif test_name == 'serum_bilirubin':
            self.fields['serum_bilirubin_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Serum Bilirubin Result')
        elif test_name == 'serum_ast':
            self.fields['serum_ast_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Serum AST Result')
        elif test_name == 'serum_alt':
            self.fields['serum_alt_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Serum ALT Result')
        elif test_name == 'serum_alp':
            self.fields['serum_alp_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Serum ALP Result')
        elif test_name == 'serum_urea':
            self.fields['serum_urea_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Serum Urea Result')
        elif test_name == 'serum_creatinine':
            self.fields['serum_creatinine_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Serum Creatinine Result')
        elif test_name == 'complete_blood_count':
            self.fields['complete_blood_count_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Complete Blood Count Result')
        elif test_name == 'blood_grouping':
            self.fields['blood_grouping_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Blood Grouping Result')
        elif test_name == 'peripheral_thin_film':
            self.fields['peripheral_thin_film_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Peripheral Thin Film Result')
        elif test_name == 'blood_smear':
            self.fields['blood_smear_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Blood Smear Result')
        elif test_name == 'urinalysis':
            self.fields['urinalysis_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Urinalysis Result')
        elif test_name == 'stool_analysis':
            self.fields['stool_analysis_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Stool Analysis Result')
        elif test_name == 'h_pylori_stool_antigen_test':
            self.fields['h_pylori_stool_antigen_test_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='H.Pylori Stool Antigen Test Result')
        elif test_name == 'antistreptolysin_test':
            self.fields['antistreptolysin_test_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Antistreptolysin Test Result')
        elif test_name == 'hepatitis_b_surface_antigen':
            self.fields['hepatitis_b_surface_antigen_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Hepatitis B Surface Antigen Result')
        elif test_name == 'malaria_rdts':
            self.fields['malaria_rdts_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Malaria RDTs Result')
        elif test_name == 'rbs':
            self.fields['rbs_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='RBS Result')
        elif test_name == 'rct':
            self.fields['rct_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='RCT Result')
        elif test_name == 'rpr':
            self.fields['rpr_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='RPR Result')
        elif test_name == 'sickling_test':
            self.fields['sickling_test_result'] = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}), label='Sickling Test Result')