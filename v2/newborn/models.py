from django.db import models
from django.contrib.auth.models import User
from datetime import date

HIV_STATUS = [
    ('NEG', 'Negative'),
    ('POS', 'Positive'),
    ('UNS', 'Not sure'),
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
    contact = models.IntegerField(default=28)

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
    nin_no = models.CharField(max_length=100)
    occupation = models.CharField(max_length=3, choices=OCCUPATION)
    location = models.ForeignKey(MotherLocation, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class Newborn(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    birth_weight = models.IntegerField()
    admission_date = models.DateField()
    age_in_days = models.IntegerField(default=0)
    gestation_age = models.IntegerField(default=28)
    diagnosis = models.CharField(max_length=100)
    discharge_date = models.DateField()
    mother = models.ForeignKey(MotherDetails, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ': ' + self.diagnosis

    class Meta:
        ordering = ['admission_date']

class LabInvestigation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    serology = models.TextField(max_length=100, choices=SEROLOGY_CHOICES, null=True,blank=True)
    microbiology = models.TextField(max_length=100, choices=MICROBIOLOGY_CHOICES,null=True, blank=True)
    chemistry = models.TextField(max_length=100, choices=CHEMISTRY_CHOICES, null=True,blank=True)
    hematology = models.TextField(max_length=100, choices=HEMATOLOGY_CHOICES, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
