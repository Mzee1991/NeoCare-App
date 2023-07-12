from django.forms import ModelForm
from django import forms
from .models import Newborn, MotherDetails, MotherLocation, LabInvestigation, Patient, NewbornExam, AntenatalHistory, District, Subcounty, Parish, Village
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

class MotherLocationForm(forms.ModelForm):
    # Fields without initial querysets
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label='---------')
    subcounty = forms.ModelChoiceField(queryset=Subcounty.objects.none(), empty_label='---------')
    parish = forms.ModelChoiceField(queryset=Parish.objects.none(), empty_label='---------')
    village = forms.ModelChoiceField(queryset=Village.objects.none(), empty_label='---------')

    class Meta:
        model = MotherLocation
        fields = ['country', 'district', 'subcounty', 'parish', 'village', 'contact', 'nin_no']
        widgets = {
            # Widget definitions
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        print('We are clear')
        print()
        #print('Instance:', instance.district)
        if instance:
            district = instance.district
            self.fields['district'].queryset = District.objects.filter(pk=district.pk)
            print('In the form, the district is', self.fields['district'].queryset)
            self.fields['subcounty'].queryset = Subcounty.objects.filter(district=district)
            self.fields['parish'].queryset = Parish.objects.filter(subcounty__district=district)
            self.fields['village'].queryset = Village.objects.filter(parish__subcounty__district=district)
        else:
            print('The else part is working')
            self.fields['subcounty'].queryset = Subcounty.objects.none()
            self.fields['parish'].queryset = Parish.objects.none()
            self.fields['village'].queryset = Village.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        district_name = cleaned_data.get('district')
        subcounty_id = cleaned_data.get('subcounty')
        parish_id = cleaned_data.get('parish')
        village_id = cleaned_data.get('village')
        print('District', district_name)
        print('Subcounty', subcounty_id)


        if district_name and subcounty_id and parish_id and village_id:
            try:
                district_obj = District.objects.get(name=district_name)
                subcounty_obj = Subcounty.objects.get(district=district_obj, id=subcounty_id)
                parish_obj = Parish.objects.get(subcounty=subcounty_obj, id=parish_id)
                village_obj = Village.objects.get(parish=parish_obj, id=village_id)

                self.instance.district = district_obj
                self.instance.subcounty = subcounty_obj
                self.instance.parish = parish_obj
                self.instance.village = village_obj

            except (Subcounty.DoesNotExist, Parish.DoesNotExist, Village.DoesNotExist):
                raise forms.ValidationError("Invalid choice selected.")

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

#class LabInvestigationForm(ModelForm):
 #   def clean(self):
  #      cleaned_data = super().clean()
   #     serology = cleaned_data.get('serology')
    #    microbiology = cleaned_data.get('microbiology')
     #   chemistry = cleaned_data.get('chemistry')
      #  hematology = cleaned_data.get('hematology')
#
 #       if not any([serology, microbiology, chemistry, hematology]):
  #          raise forms.ValidationError("Please select at least one option.")
#
#
   # class Meta:
 #       model = LabInvestigation
  #      fields = ['serology', 'microbiology', 'chemistry', 'hematology']
   #     widgets = {
    #            'serology': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
     #           'microbiology': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
      #          'chemistry': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
       #         'hematology': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        #}



#class BirthRecordForm(forms.ModelForm):
 #   class Meta:
  #      model = BirthRecord
   #     fields = ['place_of_birth', 'name_of_health_facility', 'location_of_health_facility', 'mode_of_delivery',
    #              'indication_for_csection', 'time_btn_cs_and_delivery', 'resuscitation', 'length_of_resuscitation',
     #             'was_ox_connected', 'referral', 'reason_for_referral', 'date_and_time_of_referral', 'mean_of_transport']
      #  widgets = {
       #     'place_of_birth': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
        #    'mode_of_delivery': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
         #   'resuscitation': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
          #  'referral': forms.Select(attrs={'class': 'form-control', 'onchange': 'showHideFields()'}),
        #}


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
