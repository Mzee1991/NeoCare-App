from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from newborn.models import NewbornAdmission


class LabRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='lab_requests')  # Add related_name
    neonate = models.ForeignKey(NewbornAdmission, on_delete=models.CASCADE, null=True, related_name='lab_requests') 
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
    neonate = models.ForeignKey(NewbornAdmission, on_delete=models.CASCADE, null=True, related_name='lab_results')  # Add related_name
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='lab_results')

    serology_rpr_result = models.CharField(verbose_name='RPR', max_length=100, blank=True, null=True)
    serology_rct_result = models.CharField(verbose_name='RCT', max_length=100, blank=True, null=True)
    serology_bat_result = models.CharField(max_length=100, blank=True, null=True)
    
    microbiology_gram_stain_result = models.CharField(max_length=100, blank=True, null=True)
    microbiology_culture_result = models.CharField(max_length=100, blank=True, null=True)
    
    chemistry_serum_electrolytes_result = models.CharField(max_length=100, blank=True, null=True)
    chemistry_serum_urea_result = models.CharField(max_length=100, blank=True, null=True)
    chemistry_serum_creatinine_result = models.CharField(max_length=100, blank=True, null=True)
    chemistry_urinalysis_result = models.CharField(max_length=100, blank=True, null=True)
