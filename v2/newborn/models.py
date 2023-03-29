from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.auth.models import User
from datetime import date

HIV_STATUS = [
    ('NEG', 'Negative'),
    ('POS', 'Positive'),
    ('UNS', 'Not sure'),
]
SEX = [
    ('F', 'FEMALE'),
    ('M', 'MALE'),
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
    ('PR', 'Primary'),
    ('SR', 'Secondary'),
    ('DP', 'Diploma'),
    ('BA', 'Bachelors Degree'),
    ('MA', 'Masters'),
]
OCCUPATION = [
    ('HW', 'Health Worker'),
    ('TR', 'Teacher'),
    ('LW', 'Lawyer'),
    ('AC', 'Accountant'),
    ('BU', 'Business'),
    ('FMR', 'Farmer'),
    ('ENG', 'Engineer'),
    ('SW', 'Social Worker'),
    ('OTH', 'Other'),
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

class MotherLocation(models.Model):
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    subcounty = models.CharField(max_length=100)
    parish = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    nin_no = models.CharField(max_length=100, default='CMX10000000')
    contact = models.CharField(max_length=100, default='+256 ')

    def __str__(self):
        return self.district

class MotherDetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=28)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP)
    parity = models.CharField(max_length=100)
    number_of_living_children = models.CharField(max_length=100)
    hiv_status = models.CharField(max_length=3, choices=HIV_STATUS)
    level_of_education = models.CharField(max_length=2, choices=LEVEL_OF_EDUCATION)
    occupation = models.CharField(max_length=3, choices=OCCUPATION)
    location = models.ForeignKey(MotherLocation, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class Newborn(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, choices=SEX)
    date_of_birth = models.DateField()
    birth_weight = models.DecimalField(max_digits=2, decimal_places=1)
    admission_date = models.DateField()
    age_in_days = models.IntegerField(default=0)
    gestation_age = models.IntegerField(default=28)
    diagnosis = models.CharField(max_length=100)
    mother = models.ForeignKey(MotherDetails, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ': ' + self.diagnosis

    class Meta:
        ordering = ['admission_date']


class LabInvestigation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    serology = MultiSelectField(max_length=100, choices=SEROLOGY_CHOICES)
    microbiology = MultiSelectField(max_length=100, choices=MICROBIOLOGY_CHOICES)
    chemistry = MultiSelectField(max_length=100, choices=CHEMISTRY_CHOICES)
    hematology = MultiSelectField(max_length=100, choices=HEMATOLOGY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    symptoms = models.TextField(blank=True)
    general_findings = models.TextField(blank=True)
    respiratory_findings = models.TextField(blank=True)
    cardiovascular_findings = models.TextField(blank=True)
    abdominal_findings = models.TextField(blank=True)

class BirthRecord(models.Model):
    PLACE_OF_BIRTH_CHOICES = [
        ('Home', 'Home'),
        ('Health Facility', 'Health Facility'),
        ('Road side', 'Road side')
    ]
    MODE_OF_DELIVERY_CHOICES = [
        ('Ceaserean section', 'Ceaserean section'),
        ('SVD', 'SVD'),
        ('Assisted Delivery', 'Assisted Delivery')
    ]
    INDICATION_FOR_CSECTION_CHOICES = [
        ('Preeclampsia', 'Preeclampsia'),
        ('Preterm labour', 'Preterm labour')
    ]
    TIME_BTN_CS_AND_DELIVERY_CHOICES = [
        ('less than 30min', 'less than 30min'),
        ('30min to 1 hour', '30min to 1 hour'),
        ('more than 1 hour', 'more than 1 hour')
    ]
    LENGTH_OF_RESUSCITATION_CHOICES = [
        ('less than 10min', 'less than 10min'),
        ('btn 10min to 15 min', 'btn 10min to 15 min'),
        ('more than 15min', 'more than 15min')
    ]
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    place_of_birth = models.CharField(choices=PLACE_OF_BIRTH_CHOICES, max_length=20)
    name_of_health_facility = models.CharField(blank=True, null=True, max_length=100)
    location_of_health_facility = models.CharField(blank=True, null=True, max_length=100)
    mode_of_delivery = models.CharField(choices=MODE_OF_DELIVERY_CHOICES, max_length=20)
    indication_for_csection = models.CharField(choices=INDICATION_FOR_CSECTION_CHOICES, blank=True, null=True, max_length=20)
    time_btn_cs_and_delivery = models.CharField(choices=TIME_BTN_CS_AND_DELIVERY_CHOICES, blank=True, null=True, max_length=20)
    resuscitation = models.CharField(choices=YES_NO_CHOICES, max_length=3)
    length_of_resuscitation = models.CharField(choices=LENGTH_OF_RESUSCITATION_CHOICES, blank=True, null=True, max_length=30)
    was_ox_connected = models.CharField(choices=YES_NO_CHOICES, blank=True, null=True, max_length=3)
    referral = models.CharField(choices=YES_NO_CHOICES, max_length=3)
    reason_for_referral = models.CharField(blank=True, null=True, max_length=100)
    date_and_time_of_referral = models.DateTimeField(blank=True, null=True)
    mean_of_transport = models.CharField(blank=True, null=True, max_length=100)
