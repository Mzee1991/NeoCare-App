from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from newborn.models import MotherLocation

class Registration(models.Model):
    registration_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField()
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    location = models.ForeignKey(MotherLocation, on_delete=models.CASCADE)
    RELIGION_CHOICES = [
        ('Catholic', 'Catholic'),
        ('Anglican', 'Anglican'),
        ('Muslim', 'Muslim'),
        ('Seventh Day Adventist', 'Seventh Day Adventist'),
        ('Orthodox', 'Orthodox'),
        ('Pentecostal', 'Pentecostal'),
        ('Others', 'Others'),
    ]
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    tribe = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=100)
    RELATIONSHIP_CHOICES = [
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Aunt', 'Aunt'),
        ('Uncle', 'Uncle'),
        ('Grandfather', 'Grandfather'),
        ('Grandmother', 'Grandmother'),
        ('Guardian', 'Guardian'),
        ('Other Relative', 'Other Relative'),
    ]
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrar')  # Assuming you have a User model

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Measurements(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Compulsory
    height = models.DecimalField(max_digits=5, decimal_places=2)  # Compulsory
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)  # Compulsory
    head_circumference = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    respiration = models.PositiveIntegerField(blank=True, null=True)
    pulse = models.PositiveIntegerField(blank=True, null=True)
    muac = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    oxygen = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    datetime_taken = models.DateTimeField(auto_now_add=True)  # Automatically saves the date and time of measurement

    def __str__(self):
        return f"Measurements for {self.registration.first_name} {self.registration.second_name}"


class LabRequestChildren(models.Model):
    serum_electrolytes_requested = models.BooleanField(default=False, verbose_name="Serum Electrolytes")
    serum_bilirubin_requested = models.BooleanField(default=False, verbose_name="Serum Bilirubin")
    serum_ast_requested = models.BooleanField(default=False, verbose_name="Serum AST")
    serum_alt_requested = models.BooleanField(default=False, verbose_name="Serum ALT")
    serum_alp_requested = models.BooleanField(default=False, verbose_name="Serum ALP")
    serum_urea_requested = models.BooleanField(default=False, verbose_name="Serum Urea")
    serum_creatinine_requested = models.BooleanField(default=False, verbose_name="Serum Creatinine")
    complete_blood_count_requested = models.BooleanField(default=False, verbose_name="Complete Blood Count")
    blood_grouping_requested = models.BooleanField(default=False, verbose_name="Blood Grouping")
    peripheral_thin_film_requested = models.BooleanField(default=False, verbose_name="Peripheral Thin Film")
    blood_smear_requested = models.BooleanField(default=False, verbose_name="Blood Smear")
    urinalysis_requested = models.BooleanField(default=False, verbose_name="Urinalysis")
    stool_analysis_requested = models.BooleanField(default=False, verbose_name="Stool Analysis")
    h_pylori_stool_antigen_test_requested = models.BooleanField(default=False, verbose_name="H.Pylori Stool Antigen Test")
    antistreptolysin_test_requested = models.BooleanField(default=False, verbose_name="Antistreptolysin Test")
    hepatitis_b_surface_antigen_requested = models.BooleanField(default=False, verbose_name="Hepatitis B Surface Antigen")
    malaria_rdts_requested = models.BooleanField(default=False, verbose_name="Malaria RDTs")
    rbs_requested = models.BooleanField(default=False, verbose_name="RBS")
    rct_requested = models.BooleanField(default=False, verbose_name="RCT")
    rpr_requested = models.BooleanField(default=False, verbose_name="RPR")
    sickling_test_requested = models.BooleanField(default=False, verbose_name="Sickling Test")

    # Additional fields
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='lab_requests_children')
    child = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, related_name='lab_requests_children')
    timestamp = models.DateTimeField(default=timezone.now)

    def get_test_name(self):
        # Define a mapping of field names to test names
        field_to_test_name = {
            'serum_electrolytes_requested': 'Serum Electrolytes',
            'serum_bilirubin_requested': 'Serum Bilirubin',
            'serum_ast_requested': 'Serum AST',
            'serum_alt_requested': 'Serum ALT',
            'serum_alp_requested': 'Serum ALP',
            'serum_urea_requested': 'Serum Urea',
            'serum_creatinine_requested': 'Serum Creatinine',
            'complete_blood_count_requested': 'Complete Blood Count',
            'blood_grouping_requested': 'Blood Grouping',
            'peripheral_thin_film_requested': 'Peripheral Thin Film',
            'blood_smear_requested': 'Blood Smear',
            'urinalysis_requested': 'Urinalysis',
            'stool_analysis_requested': 'Stool Analysis',
            'h_pylori_stool_antigen_test_requested': 'H.Pylori Stool Antigen Test',
            'antistreptolysin_test_requested': 'Antistreptolysin Test',
            'hepatitis_b_surface_antigen_requested': 'Hepatitis B Surface Antigen',
            'malaria_rdts_requested': 'Malaria RDTs',
            'rbs_requested': 'RBS',
            'rct_requested': 'RCT',
            'rpr_requested': 'RPR',
            'sickling_test_requested': 'Sickling Test',
        }

        # Loop through the fields and return the test name if it's True
        for field, test_name in field_to_test_name.items():
            if getattr(self, field):
                return test_name

        return "Unknown Test"  # Return a default test name if no test is selected

    def __str__(self):
        return f"Lab Requests for {self.child.first_name} {self.child.second_name}"


class LabResultChildren(models.Model):
    serum_electrolytes_result = models.CharField(max_length=100, blank=True, null=True)
    serum_bilirubin_result = models.CharField(max_length=100, blank=True, null=True)
    serum_ast_result = models.CharField(max_length=100, blank=True, null=True)
    serum_alt_result = models.CharField(max_length=100, blank=True, null=True)
    serum_alp_result = models.CharField(max_length=100, blank=True, null=True)
    serum_urea_result = models.CharField(max_length=100, blank=True, null=True)
    serum_creatinine_result = models.CharField(max_length=100, blank=True, null=True)
    complete_blood_count_result = models.CharField(max_length=100, blank=True, null=True)
    blood_grouping_result = models.CharField(max_length=100, blank=True, null=True)
    peripheral_thin_film_result = models.CharField(max_length=100, blank=True, null=True)
    blood_smear_result = models.CharField(max_length=100, blank=True, null=True)
    urinalysis_result = models.CharField(max_length=100, blank=True, null=True)
    stool_analysis_result = models.CharField(max_length=100, blank=True, null=True)
    h_pylori_stool_antigen_test_result = models.CharField(max_length=100, blank=True, null=True)
    antistreptolysin_test_result = models.CharField(max_length=100, blank=True, null=True)
    hepatitis_b_surface_antigen_result = models.CharField(max_length=100, blank=True, null=True)
    malaria_rdts_result = models.CharField(max_length=100, blank=True, null=True)
    rbs_result = models.CharField(max_length=100, blank=True, null=True)
    rct_result = models.CharField(max_length=100, blank=True, null=True)
    rpr_result = models.CharField(max_length=100, blank=True, null=True)
    sickling_test_result = models.CharField(max_length=100, blank=True, null=True)

    # ForeignKey fields
    lab_request = models.ForeignKey(LabRequestChildren, on_delete=models.CASCADE)
    child = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, related_name='lab_results_children')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='lab_results_children')

    def result_data(self):
        # Create a dictionary to store the test results
        result_data = {
            'serum_electrolytes': self.serum_electrolytes_result,
            'serum_bilirubin': self.serum_bilirubin_result,
            'serum_ast': self.serum_ast_result,
            'serum_alt': self.serum_alt_result,
            'serum_alp': self.serum_alp_result,
            'serum_urea': self.serum_urea_result,
            'serum_creatinine': self.serum_creatinine_result,
            'complete_blood_count': self.complete_blood_count_result,
            'blood_grouping': self.blood_grouping_result,
            'peripheral_thin_film': self.peripheral_thin_film_result,
            'blood_smear': self.blood_smear_result,
            'urinalysis': self.urinalysis_result,
            'stool_analysis': self.stool_analysis_result,
            'h_pylori_stool_antigen_test': self.h_pylori_stool_antigen_test_result,
            'antistreptolysin_test': self.antistreptolysin_test_result,
            'hepatitis_b_surface_antigen': self.hepatitis_b_surface_antigen_result,
            'malaria_rdts': self.malaria_rdts_result,
            'rbs': self.rbs_result,
            'rct': self.rct_result,
            'rpr': self.rpr_result,
            'sickling_test': self.sickling_test_result,
        }

        # Remove tests with no results (empty strings)
        result_data = {test_name: result for test_name, result in result_data.items() if result}

        return result_data

    def __str__(self):
        return f"Lab Results for {self.child.first_name} {self.child.second_name}"
