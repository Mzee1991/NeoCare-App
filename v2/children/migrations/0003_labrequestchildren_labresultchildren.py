# Generated by Django 4.2.2 on 2023-10-18 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('children', '0002_measurements'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabRequestChildren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serum_electrolytes_requested', models.BooleanField(default=False, verbose_name='Serum Electrolytes')),
                ('serum_bilirubin_requested', models.BooleanField(default=False, verbose_name='Serum Bilirubin')),
                ('serum_ast_requested', models.BooleanField(default=False, verbose_name='Serum AST')),
                ('serum_alt_requested', models.BooleanField(default=False, verbose_name='Serum ALT')),
                ('serum_alp_requested', models.BooleanField(default=False, verbose_name='Serum ALP')),
                ('serum_urea_requested', models.BooleanField(default=False, verbose_name='Serum Urea')),
                ('serum_creatinine_requested', models.BooleanField(default=False, verbose_name='Serum Creatinine')),
                ('complete_blood_count_requested', models.BooleanField(default=False, verbose_name='Complete Blood Count')),
                ('blood_grouping_requested', models.BooleanField(default=False, verbose_name='Blood Grouping')),
                ('peripheral_thin_film_requested', models.BooleanField(default=False, verbose_name='Peripheral Thin Film')),
                ('blood_smear_requested', models.BooleanField(default=False, verbose_name='Blood Smear')),
                ('urinalysis_requested', models.BooleanField(default=False, verbose_name='Urinalysis')),
                ('stool_analysis_requested', models.BooleanField(default=False, verbose_name='Stool Analysis')),
                ('h_pylori_stool_antigen_test_requested', models.BooleanField(default=False, verbose_name='H.Pylori Stool Antigen Test')),
                ('antistreptolysin_test_requested', models.BooleanField(default=False, verbose_name='Antistreptolysin Test')),
                ('hepatitis_b_surface_antigen_requested', models.BooleanField(default=False, verbose_name='Hepatitis B Surface Antigen')),
                ('malaria_rdts_requested', models.BooleanField(default=False, verbose_name='Malaria RDTs')),
                ('rbs_requested', models.BooleanField(default=False, verbose_name='RBS')),
                ('rct_requested', models.BooleanField(default=False, verbose_name='RCT')),
                ('rpr_requested', models.BooleanField(default=False, verbose_name='RPR')),
                ('sickling_test_requested', models.BooleanField(default=False, verbose_name='Sickling Test')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_requests_children', to=settings.AUTH_USER_MODEL)),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_requests_children', to='children.registration')),
            ],
        ),
        migrations.CreateModel(
            name='LabResultChildren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serum_electrolytes_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serum_bilirubin_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serum_ast_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serum_alt_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serum_alp_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serum_urea_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serum_creatinine_result', models.CharField(blank=True, max_length=100, null=True)),
                ('complete_blood_count_result', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_grouping_result', models.CharField(blank=True, max_length=100, null=True)),
                ('peripheral_thin_film_result', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_smear_result', models.CharField(blank=True, max_length=100, null=True)),
                ('urinalysis_result', models.CharField(blank=True, max_length=100, null=True)),
                ('stool_analysis_result', models.CharField(blank=True, max_length=100, null=True)),
                ('h_pylori_stool_antigen_test_result', models.CharField(blank=True, max_length=100, null=True)),
                ('antistreptolysin_test_result', models.CharField(blank=True, max_length=100, null=True)),
                ('hepatitis_b_surface_antigen_result', models.CharField(blank=True, max_length=100, null=True)),
                ('malaria_rdts_result', models.CharField(blank=True, max_length=100, null=True)),
                ('rbs_result', models.CharField(blank=True, max_length=100, null=True)),
                ('rct_result', models.CharField(blank=True, max_length=100, null=True)),
                ('rpr_result', models.CharField(blank=True, max_length=100, null=True)),
                ('sickling_test_result', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_results_children', to=settings.AUTH_USER_MODEL)),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_results_children', to='children.registration')),
                ('lab_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.labrequestchildren')),
            ],
        ),
    ]
