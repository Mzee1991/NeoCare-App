from django.forms import ModelForm
from django import forms
from .models import Newborn, NewbornAdmission, MotherDetails, MotherLocation, LabInvestigation, Patient, NewbornExam, AntenatalHistory, District, Subcounty, Parish, Village, CountyMunicipality, MothersAntenatalDetails
from .models import SEROLOGY_CHOICES, MICROBIOLOGY_CHOICES, CHEMISTRY_CHOICES, HEMATOLOGY_CHOICES


class AntenatalHistoryForm(forms.ModelForm):
    class Meta:
        model = AntenatalHistory
        fields = [
            'attended',
            'number_of_times_attended',
            'attended_where',
            'conditions_during_pregnancy',
            'received_tetanus_toxoid',
            'screened_for_syphilis',
            'received_fansidar',
        ]

    attended = forms.ChoiceField(choices=AntenatalHistory.Yes_No_CHOICES, widget=forms.RadioSelect)
    received_tetanus_toxoid = forms.ChoiceField(choices=AntenatalHistory.Yes_No_CHOICES, widget=forms.RadioSelect)
    screened_for_syphilis = forms.ChoiceField(choices=AntenatalHistory.Yes_No_CHOICES, widget=forms.RadioSelect)
    received_fansidar = forms.ChoiceField(choices=AntenatalHistory.Yes_No_CHOICES, widget=forms.RadioSelect)

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
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label='---------')
    county_municipality = forms.ModelChoiceField(queryset=CountyMunicipality.objects.none(), empty_label='---------')
    subcounty = forms.ModelChoiceField(queryset=Subcounty.objects.none(), empty_label='---------')
    parish = forms.ModelChoiceField(queryset=Parish.objects.none(), empty_label='---------')
    village = forms.ModelChoiceField(queryset=Village.objects.none(), empty_label='---------')

    class Meta:
        model = MotherLocation
        fields = ['country', 'district', 'county_municipality', 'subcounty', 'parish', 'village', 'contact', 'nin_no']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'county_municipality': forms.Select(attrs={'class': 'form-control'}),
            'subcounty': forms.Select(attrs={'class': 'form-control'}),
            'parish': forms.Select(attrs={'class': 'form-control'}),
            'village': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'nin_no': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super().__init__(*args, **kwargs)

        instance = kwargs.get('instance')
        if is_update and instance:
            self.fields['district'].disabled = True  # Disable the district field to prevent changes
            if instance.district:
                district_id = instance.district_id
                self.fields['county_municipality'].queryset = CountyMunicipality.objects.filter(district_id=district_id)
                if instance.county_municipality:
                    county_municipality_id = instance.county_municipality_id
                    self.fields['subcounty'].queryset = Subcounty.objects.filter(county_municipality_id=county_municipality_id)
                    if instance.subcounty:
                        subcounty_id = instance.subcounty_id
                        self.fields['parish'].queryset = Parish.objects.filter(subcounty_id=subcounty_id)
                        if instance.parish:
                            parish_id = instance.parish_id
                            self.fields['village'].queryset = Village.objects.filter(parish_id=parish_id)
        else:
            if 'district' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    self.fields['county_municipality'].queryset = CountyMunicipality.objects.filter(district_id=district_id)
                except (ValueError, TypeError):
                    pass
            if 'county_municipality' in self.data:
                try:
                    county_municipality_id = int(self.data.get('county_municipality'))
                    self.fields['subcounty'].queryset = Subcounty.objects.filter(county_municipality_id=county_municipality_id)
                except (ValueError, TypeError):
                    pass
            if 'subcounty' in self.data:
                try:
                    subcounty_id = int(self.data.get('subcounty'))
                    self.fields['parish'].queryset = Parish.objects.filter(subcounty_id=subcounty_id)
                except (ValueError, TypeError):
                    pass
            if 'parish' in self.data:
                try:
                    parish_id = int(self.data.get('parish'))
                    self.fields['village'].queryset = Village.objects.filter(parish_id=parish_id)
                except (ValueError, TypeError):
                    pass
            self.fields['district'].queryset = District.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        district = cleaned_data.get('district')
        county_municipality = cleaned_data.get('county_municipality')
        subcounty = cleaned_data.get('subcounty')
        parish = cleaned_data.get('parish')
        village = cleaned_data.get('village')

        if not district:
            raise forms.ValidationError("Please select a district.")
        if not county_municipality:
            raise forms.ValidationError("Please select a county/municipality.")
        if not subcounty:
            raise forms.ValidationError("Please select a subcounty.")
        if not parish:
            raise forms.ValidationError("Please select a parish.")
        if not village:
            raise forms.ValidationError("Please select a village.")

        return cleaned_data

class LabInvestigationForm(ModelForm):
    class Meta:
        model = LabInvestigation
        fields = [
            'serology_rpr',
            'serology_rct',
            'serology_bat',
            'microbiology_gram_stain',
            'microbiology_culture',
            'chemistry_serum_electrolytes',
            'chemistry_serum_urea',
            'chemistry_serum_creatinine',
            'chemistry_urinalysis',
        ]


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

class NewbornForm(forms.ModelForm):
    class Meta:
        model = Newborn
        fields = ('admission_date','name','sex','birth_weight','delivery_date', 'place_of_birth', 'mode_of_delivery', 'resuscitated', 'referral')

    admission_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    delivery_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    place_of_birth = forms.ChoiceField(choices=Newborn.PLACE_OF_BIRTH_CHOICES)
    mode_of_delivery = forms.ChoiceField(choices=Newborn.MODE_OF_DELIVERY_CHOICES)
    resuscitated = forms.ChoiceField(choices=Newborn.Yes_No_CHOICES, widget=forms.RadioSelect)
    referral = forms.ChoiceField(choices=Newborn.Yes_No_CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery_date'].input_formats = ('%Y-%m-%dT%H:%M',)  # set input format for datetime-local widget
        self.fields['admission_date'].input_formats = ('%Y-%m-%dT%H:%M',)  # set input format for datetime-local widget
        mother_name = self.instance.mother.name if self.instance.mother else ""
        self.fields['name'].initial = f"B/O {mother_name}"


class NewbornExamForm(forms.ModelForm):
    class Meta:
        model = NewbornExam
        fields = [
            'weight',
            'respiratory_rate',
            'heart_rate',
            'temperature',
            'skin_color',
            'general_appearance',
            'head_and_neck',
            'chest',
            'abdomen',
            'genitalia',
            'extremities',
            'neurological_exam',
        ]


class MothersAntenatalDetailsForm(forms.ModelForm):
    class Meta:
        model = MothersAntenatalDetails
        exclude = ('mother',) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['number_attended'].required = False
        self.fields['attended_from'].required = False
        self.fields['facility_name'].required = False
        self.fields['other_conditions'].required = False
        self.fields['number_tt_received'].required = False
        self.fields['number_ipt_received'].required = False
        self.fields['hiv_test_result'].required = False
        self.fields['on_art'].required = False
        self.fields['syphilis_test_result'].required = False
        self.fields['received_treatment'].required = False # Add the form-control class for consistent styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Add JavaScript classes to the fields for event handling
        self.fields['attended'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['conditions_during_pregnancy'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['received_tt'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['received_ipt'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['screened_for_hiv'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['hiv_test_result'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['screened_for_syphilis'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['syphilis_test_result'].widget.attrs['class'] += ' dynamic-field-trigger'
    def clean(self):
        cleaned_data = super().clean()

        # Step 1: Check 'Attended' fields and related fields
        attended = cleaned_data.get('attended')
        print("Check attended", attended)
        if attended == 'Yes':
            number_attended = cleaned_data.get('number_attended')
            attended_from = cleaned_data.get('attended_from')
            facility_name = cleaned_data.get('facility_name')

            if not number_attended:
                self.add_error('number_attended', "If 'Attended' is 'Yes', 'Number of times attended' must be provided.")
            if not attended_from:
                self.add_error('attended_from', "If 'Attended' is 'Yes', 'Attended from' must be provided.")
            if not facility_name:
                self.add_error('facility_name', "If 'Attended' is 'Yes', 'Facility Name' must be provided.")

        # Step 2: Check 'Conditions during pregnancy' and 'Other conditions'
        conditions_during_pregnancy = cleaned_data.get('conditions_during_pregnancy')
        other_conditions = cleaned_data.get('other_conditions')
        if conditions_during_pregnancy == 'Others' and not other_conditions:
            self.add_error('other_conditions', "If 'Conditions during pregnancy' is 'Others', 'Specify other condition' must be provided.")

        # Step 3: Check 'Received T.T' and 'Number of times T.T received'
        received_tt = cleaned_data.get('received_tt')
        print("TT recived", received_tt)
        number_tt_received = cleaned_data.get('number_tt_received')
        if received_tt == 'Yes' and not number_tt_received:
            self.add_error('number_tt_received', "If 'Received T.T' is 'Yes', 'Number of times T.T received' must be provided.")

        # Step 4: Check 'Received IPT' and 'Number of times IPT received'
        received_ipt = cleaned_data.get('received_ipt')
        number_ipt_received = cleaned_data.get('number_ipt_received')
        if received_ipt == 'Yes' and not number_ipt_received:
            self.add_error('number_ipt_received', "If 'Received IPT' is 'Yes', 'Number of times IPT received' must be provided.")

        # Step 5: Check 'Screened for HIV' and related fields
        screened_for_hiv = cleaned_data.get('screened_for_hiv')
        hiv_test_result = cleaned_data.get('hiv_test_result')
        if screened_for_hiv == 'Yes' and not hiv_test_result:
            self.add_error('hiv_test_result', "If 'Screened for HIV' is 'Yes', 'HIV Test result' must be provided.")
        
        if hiv_test_result == 'Positive':
            on_art = cleaned_data.get('on_art')
            if not on_art:
                self.add_error('on_art', "If 'HIV Test result' is 'Positive', 'Is Mother on ART' must be provided.")

        # Step 6: Check 'Screened for Syphilis' and related fields
        screened_for_syphilis = cleaned_data.get('screened_for_syphilis')
        syphilis_test_result = cleaned_data.get('syphilis_test_result')
        if screened_for_syphilis == 'Yes' and not syphilis_test_result:
            self.add_error('syphilis_test_result', "If 'Screened for Syphilis' is 'Yes', 'Syphilis Test result' must be provided.")
        
        if syphilis_test_result == 'Positive':
            received_treatment = cleaned_data.get('received_treatment')
            if not received_treatment:
                self.add_error('received_treatment', "If 'Syphilis Test result' is 'Positive', 'Did Mother receive Treatment' must be provided.")

        return cleaned_data


class NewbornAdmissionForm(forms.ModelForm):
    class Meta:
        model = NewbornAdmission
        fields = '__all__'

    resuscitation_choices_1 = forms.BooleanField(label='Bag & Mask',required=False,widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    resuscitation_choices_2 = forms.BooleanField(label='Oxygen',required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    referral_date_time = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local', 'placeholder': 'YYYY-MM-DD HH:MM'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add the form-control class for consistent styling
        for field_name, field in self.fields.items():
            if field_name not in ('resuscitation_choices_1', 'resuscitation_choices_2', 'referral_date_time'):
                field.widget.attrs['class'] = 'form-control'

        # Add JavaScript classes to the fields for event handling
        self.fields['place_of_birth'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['mode_of_delivery'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['resuscitation_done'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['referred_in'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['means_of_transport'].widget.attrs['class'] += ' dynamic-field-trigger'
        self.fields['oxygen_transport'].widget.attrs['class'] += ' dynamic-field-trigger'

    def clean(self):
        cleaned_data = super().clean()

        # Perform cross-field validation here
        referred_in = cleaned_data.get('referred_in')
        means_of_transport = cleaned_data.get('means_of_transport')
        resuscitation_done = cleaned_data.get('resuscitation_done')
        print("Referral", referred_in)

        if referred_in == 'No':
            # If the baby was not referred, make sure referral_date_time is None
            cleaned_data['referral_date_time'] = None

        if means_of_transport == 'Public means':
            # If the transport means is "Public means," make sure oxygen_transport is None
            cleaned_data['oxygen_transport'] = None

        if resuscitation_done == 'No':
            # If resuscitation was not done, set both resuscitation_choices to False
            cleaned_data['resuscitation_choices_1'] = False
            cleaned_data['resuscitation_choices_2'] = False

        # Add more cross-field validation checks as needed

        return cleaned_data
