from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
    neonate = models.ForeignKey(Newborn, on_delete=models.CASCADE, null=True)
