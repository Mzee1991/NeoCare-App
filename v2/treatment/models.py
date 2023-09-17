from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from newborn.models import NewbornAdmission

class Prescription(models.Model):
    admission = models.ForeignKey(NewbornAdmission, on_delete=models.CASCADE, related_name='prescriptions')
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
        
    # Fields for dosing times
    start_dose_time = models.TimeField()
    second_dose_time = models.TimeField(null=True, blank=True)
    third_dose_time = models.TimeField(null=True, blank=True)
    fourth_dose_time = models.TimeField(null=True, blank=True)
    
    FREQUENCY_CHOICES = [
        ('Once Daily', 'Once Daily'),
        ('Twice Daily', 'Twice Daily'),
        ('Three Times Daily', 'Three Times Daily'),
        ('Four Times Daily', 'Four Times Daily'),
    ]
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)

    start_date = models.DateField()
    prescriber = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='prescriptions_prescribed2')

    def __str__(self):
        return self.name


class Dose1Dispensation(models.Model):
    TREATMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Given', 'Given'),
        ('Missed', 'Missed'),
    ]

    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='dose1_dispensations')
    dispenser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dose1_dispensations_given')
    dispensation_datetime = models.DateTimeField(auto_now_add=True)
    dose1_status = models.CharField(max_length=15, choices=TREATMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Dose 1 - {self.prescription.name} - Dispensed by {self.dispenser.username}"

class Dose2Dispensation(models.Model):
    TREATMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Given', 'Given'),
        ('Missed', 'Missed'),
    ]

    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='dose2_dispensations')
    dispenser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dose2_dispensations_given')
    dispensation_datetime = models.DateTimeField(auto_now_add=True)
    dose2_status = models.CharField(max_length=15, choices=TREATMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Dose 2 - {self.prescription.name} - Dispensed by {self.dispenser.username}"

class Dose3Dispensation(models.Model):
    TREATMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Given', 'Given'),
        ('Missed', 'Missed'),
    ]

    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='dose3_dispensations')
    dispenser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dose3_dispensations_given')
    dispensation_datetime = models.DateTimeField(auto_now_add=True)
    dose3_status = models.CharField(max_length=15, choices=TREATMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Dose 3 - {self.prescription.name} - Dispensed by {self.dispenser.username}"

class Dose4Dispensation(models.Model):
    TREATMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Given', 'Given'),
        ('Missed', 'Missed'),
    ]

    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='dose4_dispensations')
    dispenser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dose4_dispensations_given')
    dispensation_datetime = models.DateTimeField(auto_now_add=True)
    dose4_status = models.CharField(max_length=15, choices=TREATMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Dose 4 - {self.prescription.name} - Dispensed by {self.dispenser.username}"
