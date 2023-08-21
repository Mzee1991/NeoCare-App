from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone 

HIV_STATUS = [
    ('Negative', 'Negative'),
    ('Positive', 'Positive'),
    ('Not sure', 'Not sure'),
]
SEX = [
    ('FEMALE', 'FEMALE'),
    ('MALE', 'MALE'),
]
BLOOD_GROUP = [
    ('A+', 'A RhD+'),
    ('B+', 'B RhD+'),
    ('AB+', 'AB RhD+'),
    ('O+', 'O RhD+'),
    ('A-', 'A RhD-'),
    ('B-', 'B RhD-'),
    ('AB-', 'AB RhD-'),
    ('O-', 'O RhD-'),
]
LEVEL_OF_EDUCATION = [
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('Diploma', 'Diploma'),
    ('Bachelors Degree', 'Bachelors Degree'),
    ('Masters', 'Masters'),
]
OCCUPATION = [
    ('Health Worker', 'Health Worker'),
    ('Teacher', 'Teacher'),
    ('Lawyer', 'Lawyer'),
    ('Accountant', 'Accountant'),
    ('Business', 'Business'),
    ('Farmer', 'Farmer'),
    ('Engineer', 'Engineer'),
    ('Social Worker', 'Social Worker'),
    ('Other', 'Other'),
]
SEROLOGY_CHOICES = [
        ('RPR', 'RPR'),
        ('RCT', 'RCT'),
        ('BAT', 'BAT'),
    ]
MICROBIOLOGY_CHOICES = [
	('Gram stain', 'Gram stain'),
    ('Culture', 'Culture'),
]
CHEMISTRY_CHOICES = [
	('Serum electrolytes', 'Serum electrolytes'),
    ('Serum Urea', 'Serum Urea'),
    ('Serum creatinine', 'Serum creatinine'),
    ('Urinalysis', 'Urinalysis'),
]
HEMATOLOGY_CHOICES = [
	('CBC', 'CBC'),
    ('Blood grouping', 'Blood grouping'),
]
attended_where_choices = [
        ('Hospital', 'Hospital'),
        ('Health Centre', 'Health Centre'),
        ('Private Clinic', 'Private Clinic'),
]
conditions_during_pregnancy_choices = [
        ('Diabetes', 'Diabetes'),
        ('HTN', 'HTN'),
        ('Pre-eclampsia', 'Pre-eclampsia'),
        ('APH', 'APH'),
        ('Malaria', 'Malaria'),
        ('Uneventful', 'Uneventful'),
        ('Other', 'Other'),
]


class District(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CountyMunicipality(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcounty(models.Model):
    county_municipality = models.ForeignKey(CountyMunicipality, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Parish(models.Model):
    subcounty = models.ForeignKey(Subcounty, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Village(models.Model):
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MotherLocation(models.Model):
    country = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    county_municipality = models.ForeignKey(CountyMunicipality, on_delete=models.CASCADE)
    subcounty = models.ForeignKey(Subcounty, on_delete=models.CASCADE)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    nin_no = models.CharField(max_length=100, default='CMX10000000')
    contact = models.CharField(max_length=100, default='+256 ')

    def __str__(self):
        return self.district.name


class MotherDetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=28)
    blood_group = models.CharField(max_length=50, choices=BLOOD_GROUP)
    parity = models.CharField(max_length=100)
    number_of_living_children = models.CharField(max_length=100)
    hiv_status = models.CharField(max_length=50, choices=HIV_STATUS)
    level_of_education = models.CharField(max_length=50, choices=LEVEL_OF_EDUCATION)
    occupation = models.CharField(max_length=50, choices=OCCUPATION)
    location = models.ForeignKey(MotherLocation, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name


class AntenatalHistory(models.Model):
    Yes_No_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    mother = models.ForeignKey(MotherDetails, on_delete=models.CASCADE, null=True)
    attended = models.CharField(max_length=100, choices=Yes_No_CHOICES)
    number_of_times_attended = models.PositiveIntegerField(default=0)
    attended_where = models.CharField(max_length=20, choices=attended_where_choices)
    conditions_during_pregnancy = models.CharField(max_length=20, choices=conditions_during_pregnancy_choices)
    received_tetanus_toxoid = models.CharField(max_length=100, choices=Yes_No_CHOICES)
    screened_for_syphilis = models.CharField(max_length=100, choices=Yes_No_CHOICES)
    received_fansidar = models.CharField(max_length=100, choices=Yes_No_CHOICES)

    def __str__(self):
        return f"Antenatal History of {self.mother}"



class Newborn(models.Model):
    PLACE_OF_BIRTH_CHOICES = (
        ('Hospital', 'Hospital'),
        ('Home', 'Home'),
        ('Along the road', 'Along the road'),
    )

    MODE_OF_DELIVERY_CHOICES = (
        ('Vaginal', 'Vaginal'),
        ('C-Section', 'C-Section'),
        ('Assisted Vaginal Delivery', 'Assisted Vaginal Delivery'),
    )
    
    Yes_No_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    
    admission_date = models.DateTimeField()
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=SEX)
    birth_weight = models.DecimalField(max_digits=2, decimal_places=1)
    delivery_date = models.DateTimeField()
    place_of_birth = models.CharField(max_length=100, choices=PLACE_OF_BIRTH_CHOICES)
    mode_of_delivery = models.CharField(max_length=100, choices=MODE_OF_DELIVERY_CHOICES)
    resuscitated = models.CharField(max_length=100, choices=Yes_No_CHOICES)
    referral = models.CharField(max_length=100, choices=Yes_No_CHOICES)
    mother = models.ForeignKey(MotherDetails, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Delivery to {self.place_of_birth}, {self.mode_of_delivery}"


class NewbornAdmission(models.Model):
    PLACE_OF_BIRTH_CHOICES = [
        ('Hospital', 'Hospital'),
        ('Along the road', 'Along the road'),
        ('Home', 'Home'),
    ]

    MODE_OF_DELIVERY_CHOICES = [
        ('SVD', 'SVD (Spontaneous Vaginal Delivery)'),
        ('C/S', 'C/S (Caesarean Section)'),
    ]

    MEANS_OF_TRANSPORT_CHOICES = [
        ('Ambulance', 'Ambulance'),
        ('Public means', 'Public means'),
    ]

    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    SEX = [
        ('M', 'M'),
        ('F', 'F'),
    ]

    admission_date = models.DateTimeField()
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=SEX)
    birth_weight = models.DecimalField(max_digits=2, decimal_places=1)
    delivery_date = models.DateTimeField()
    place_of_birth = models.CharField(max_length=20, choices=PLACE_OF_BIRTH_CHOICES)
    hospital_name = models.CharField(max_length=100, blank=True, null=True)
    mode_of_delivery = models.CharField(max_length=3, choices=MODE_OF_DELIVERY_CHOICES)
    indication = models.CharField(max_length=100, blank=True, null=True)
    resuscitation_done = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    resuscitation_choices_1 = models.BooleanField(verbose_name='Bag&Mask', default=False, blank=True)
    resuscitation_choices_2 = models.BooleanField(verbose_name='Oxygen', default=False, blank=True)
    referred_in = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    facility_name = models.CharField(max_length=100, blank=True, null=True)
    referral_date_time = models.DateTimeField(blank=True, null=True)
    reason_for_referral = models.CharField(max_length=100, blank=True, null=True)
    means_of_transport = models.CharField(max_length=20, choices=MEANS_OF_TRANSPORT_CHOICES, blank=True, null=True)
    oxygen_transport = models.CharField(max_length=3, choices=YES_NO_CHOICES, blank=True, null=True)
    mother = models.ForeignKey(MotherDetails, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.place_of_birth} - {self.mode_of_delivery}"


class LabRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neonate = models.ForeignKey(NewbornAdmission, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    serology_rpr_requested = models.BooleanField(verbose_name='RPR', default=False)
    serology_rct_requested = models.BooleanField(verbose_name='RCT', default=False)
    serology_bat_requested = models.BooleanField(verbose_name='BAT', default=False)
    
    microbiology_gram_stain_requested = models.BooleanField(verbose_name='Gram stain', default=False)
    microbiology_culture_requested = models.BooleanField(verbose_name='Culture', default=False)
    
    chemistry_serum_electrolytes_requested = models.BooleanField(verbose_name='Serum electrolytes', default=False)
    chemistry_serum_urea_requested = models.BooleanField(verbose_name='Serum Urea', default=False)
    chemistry_serum_creatinine_requested = models.BooleanField(verbose_name='Serum creatinine', default=False)
    chemistry_urinalysis_requested = models.BooleanField(verbose_name='Urinalysis', default=False)

class LabResult(models.Model):
    lab_request = models.ForeignKey(LabRequest, on_delete=models.CASCADE)
    neonate = models.ForeignKey(NewbornAdmission, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    serology_rpr_result = models.CharField(verbose_name='RPR', max_length=100, blank=True, null=True)
    serology_rct_result = models.CharField(verbose_name='RCT', max_length=100, blank=True, null=True)
    serology_bat_result = models.CharField(max_length=100, blank=True, null=True)
    
    microbiology_gram_stain_result = models.CharField(max_length=100, blank=True, null=True)
    microbiology_culture_result = models.CharField(max_length=100, blank=True, null=True)
    
    chemistry_serum_electrolytes_result = models.CharField(max_length=100, blank=True, null=True)
    chemistry_serum_urea_result = models.CharField(max_length=100, blank=True, null=True)
    chemistry_serum_creatinine_result = models.CharField(max_length=100, blank=True, null=True)
    chemistry_urinalysis_result = models.CharField(max_length=100, blank=True, null=True)


class Patient(models.Model):
    symptoms = models.TextField(blank=True)
    general_findings = models.TextField(blank=True)
    respiratory_findings = models.TextField(blank=True)
    cardiovascular_findings = models.TextField(blank=True)
    abdominal_findings = models.TextField(blank=True)


class NewbornExam(models.Model):
    weight = models.DecimalField(max_digits=2, decimal_places=1) # measured in kg
    respiratory_rate = models.IntegerField() # measured in breaths per minute
    heart_rate = models.IntegerField() # measured in beats per minute
    temperature = models.DecimalField(max_digits=3, decimal_places=1) # measured in degrees Celsius
    skin_color = models.CharField(max_length=100)
    general_appearance = models.CharField(max_length=100)
    head_and_neck = models.CharField(max_length=100)
    chest = models.CharField(max_length=100)
    abdomen = models.CharField(max_length=100)
    genitalia = models.CharField(max_length=100)
    extremities = models.CharField(max_length=100)
    neurological_exam = models.CharField(max_length=100)
    neonate = models.ForeignKey(NewbornAdmission, on_delete=models.CASCADE, null=True)



class MothersAntenatalDetails(models.Model):
    ATTENDED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    FACILITY_CHOICES = [
        ('Hospital', 'Hospital'),
        ('Health Centre', 'Health Centre'),
        ('Private Clinic', 'Private Clinic'),
    ]

    CONDITIONS_CHOICES = [
        ('HTN', 'HTN'),
        ('Pre-eclampsia', 'Pre-eclampsia'),
        ('Diabetes', 'Diabetes'),
        ('Others', 'Others'),
    ]

    HIV_TEST_RESULT_CHOICES = [
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    ]

    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    attended = models.CharField(max_length=3, choices=ATTENDED_CHOICES)
    number_attended = models.PositiveIntegerField(blank=True, null=True)
    attended_from = models.CharField(max_length=50, choices=FACILITY_CHOICES, blank=True, null=True)
    facility_name = models.CharField(max_length=100, null=True, blank=True)
    conditions_during_pregnancy = models.CharField(max_length=20, choices=CONDITIONS_CHOICES)
    other_conditions = models.TextField(blank=True, null=True)
    received_tt = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    number_tt_received = models.PositiveIntegerField(blank=True, null=True)
    received_ipt = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    number_ipt_received = models.PositiveIntegerField(blank=True, null=True)
    screened_for_hiv = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    hiv_test_result = models.CharField(max_length=8, choices=HIV_TEST_RESULT_CHOICES, blank=True, null=True)
    on_art = models.CharField(max_length=3, choices=YES_NO_CHOICES, blank=True, null=True)
    screened_for_syphilis = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    syphilis_test_result = models.CharField(max_length=8, choices=HIV_TEST_RESULT_CHOICES, blank=True, null=True)
    received_treatment = models.CharField(max_length=3, choices=YES_NO_CHOICES, blank=True, null=True)
    mother = models.ForeignKey(MotherDetails, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.attended} - {self.conditions_during_pregnancy}"


class Prescription(models.Model):
    admission = models.ForeignKey(NewbornAdmission, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    TREATMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Given', 'Given'),
        ('Missed', 'Missed'),
    ]
    treatment_status = models.CharField(max_length=15, choices=TREATMENT_STATUS_CHOICES)
    
    dosing_times = models.JSONField(default=list)  # Store dosing times as a JSON array

    prescriber = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='prescriptions_prescribed')
    dispenser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='prescriptions_dispensed')

    def __str__(self):
        return self.name
