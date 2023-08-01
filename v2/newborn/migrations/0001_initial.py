# Generated by Django 4.2.2 on 2023-07-31 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CountyMunicipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MotherDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=28)),
                ('blood_group', models.CharField(choices=[('A+', 'A RhD+'), ('B+', 'B RhD+'), ('AB+', 'AB RhD+'), ('O+', 'O RhD+'), ('A-', 'A RhD-'), ('B-', 'B RhD-'), ('AB-', 'AB RhD-'), ('O-', 'O RhD-')], max_length=50)),
                ('parity', models.CharField(max_length=100)),
                ('number_of_living_children', models.CharField(max_length=100)),
                ('hiv_status', models.CharField(choices=[('Negative', 'Negative'), ('Positive', 'Positive'), ('Not sure', 'Not sure')], max_length=50)),
                ('level_of_education', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Diploma', 'Diploma'), ('Bachelors Degree', 'Bachelors Degree'), ('Masters', 'Masters')], max_length=50)),
                ('occupation', models.CharField(choices=[('Health Worker', 'Health Worker'), ('Teacher', 'Teacher'), ('Lawyer', 'Lawyer'), ('Accountant', 'Accountant'), ('Business', 'Business'), ('Farmer', 'Farmer'), ('Engineer', 'Engineer'), ('Social Worker', 'Social Worker'), ('Other', 'Other')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NewbornAdmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=100)),
                ('birth_weight', models.DecimalField(decimal_places=1, max_digits=2)),
                ('delivery_date', models.DateTimeField()),
                ('place_of_birth', models.CharField(choices=[('Hospital', 'Hospital'), ('Along the road', 'Along the road'), ('Home', 'Home')], max_length=20)),
                ('hospital_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mode_of_delivery', models.CharField(choices=[('SVD', 'SVD (Spontaneous Vaginal Delivery)'), ('C/S', 'C/S (Caesarean Section)')], max_length=3)),
                ('indication', models.CharField(blank=True, max_length=100, null=True)),
                ('resuscitation_done', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('resuscitation_choices_1', models.BooleanField(blank=True, default=False, verbose_name='Bag&Mask')),
                ('resuscitation_choices_2', models.BooleanField(blank=True, default=False, verbose_name='Oxygen')),
                ('referred_in', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('facility_name', models.CharField(blank=True, max_length=100, null=True)),
                ('referral_date_time', models.DateTimeField(blank=True, null=True)),
                ('reason_for_referral', models.CharField(blank=True, max_length=100, null=True)),
                ('means_of_transport', models.CharField(blank=True, choices=[('Ambulance', 'Ambulance'), ('Public means', 'Public means')], max_length=20, null=True)),
                ('oxygen_transport', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.motherdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.TextField(blank=True)),
                ('general_findings', models.TextField(blank=True)),
                ('respiratory_findings', models.TextField(blank=True)),
                ('cardiovascular_findings', models.TextField(blank=True)),
                ('abdominal_findings', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.parish')),
            ],
        ),
        migrations.CreateModel(
            name='Subcounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county_municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newborn.countymunicipality')),
            ],
        ),
        migrations.AddField(
            model_name='parish',
            name='subcounty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.subcounty'),
        ),
        migrations.CreateModel(
            name='NewbornExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=2)),
                ('respiratory_rate', models.IntegerField()),
                ('heart_rate', models.IntegerField()),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('skin_color', models.CharField(max_length=100)),
                ('general_appearance', models.CharField(max_length=100)),
                ('head_and_neck', models.CharField(max_length=100)),
                ('chest', models.CharField(max_length=100)),
                ('abdomen', models.CharField(max_length=100)),
                ('genitalia', models.CharField(max_length=100)),
                ('extremities', models.CharField(max_length=100)),
                ('neurological_exam', models.CharField(max_length=100)),
                ('neonate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.newbornadmission')),
            ],
        ),
        migrations.CreateModel(
            name='Newborn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=100)),
                ('birth_weight', models.DecimalField(decimal_places=1, max_digits=2)),
                ('delivery_date', models.DateTimeField()),
                ('place_of_birth', models.CharField(choices=[('Hospital', 'Hospital'), ('Home', 'Home'), ('Along the road', 'Along the road')], max_length=100)),
                ('mode_of_delivery', models.CharField(choices=[('Vaginal', 'Vaginal'), ('C-Section', 'C-Section'), ('Assisted Vaginal Delivery', 'Assisted Vaginal Delivery')], max_length=100)),
                ('resuscitated', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('referral', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.motherdetails')),
            ],
        ),
        migrations.CreateModel(
            name='MothersAntenatalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('number_attended', models.PositiveIntegerField(blank=True, null=True)),
                ('attended_from', models.CharField(blank=True, choices=[('Hospital', 'Hospital'), ('Health Centre', 'Health Centre'), ('Private Clinic', 'Private Clinic')], max_length=50, null=True)),
                ('facility_name', models.CharField(blank=True, max_length=100, null=True)),
                ('conditions_during_pregnancy', models.CharField(choices=[('HTN', 'HTN'), ('Pre-eclampsia', 'Pre-eclampsia'), ('Diabetes', 'Diabetes'), ('Others', 'Others')], max_length=20)),
                ('other_conditions', models.TextField(blank=True, null=True)),
                ('received_tt', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('number_tt_received', models.PositiveIntegerField(blank=True, null=True)),
                ('received_ipt', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('number_ipt_received', models.PositiveIntegerField(blank=True, null=True)),
                ('screened_for_hiv', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('hiv_test_result', models.CharField(blank=True, choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=8, null=True)),
                ('on_art', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('screened_for_syphilis', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('syphilis_test_result', models.CharField(blank=True, choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=8, null=True)),
                ('received_treatment', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.motherdetails')),
            ],
        ),
        migrations.CreateModel(
            name='MotherLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('nin_no', models.CharField(default='CMX10000000', max_length=100)),
                ('contact', models.CharField(default='+256 ', max_length=100)),
                ('county_municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newborn.countymunicipality')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newborn.district')),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newborn.parish')),
                ('subcounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newborn.subcounty')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newborn.village')),
            ],
        ),
        migrations.AddField(
            model_name='motherdetails',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.motherlocation'),
        ),
        migrations.CreateModel(
            name='LabInvestigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serology_rpr', models.BooleanField(default=False, verbose_name='RPR')),
                ('serology_rct', models.BooleanField(default=False, verbose_name='RCT')),
                ('serology_bat', models.BooleanField(default=False, verbose_name='BAT')),
                ('microbiology_gram_stain', models.BooleanField(default=False, verbose_name='Gram stain')),
                ('microbiology_culture', models.BooleanField(default=False, verbose_name='Culture')),
                ('chemistry_serum_electrolytes', models.BooleanField(default=False, verbose_name='Serum electrolytes')),
                ('chemistry_serum_urea', models.BooleanField(default=False, verbose_name='Serum Urea')),
                ('chemistry_serum_creatinine', models.BooleanField(default=False, verbose_name='Serum creatinine')),
                ('chemistry_urinalysis', models.BooleanField(default=False, verbose_name='Urinalysis')),
                ('serology_rpr_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serology_rct_result', models.CharField(blank=True, max_length=100, null=True)),
                ('serology_bat_result', models.CharField(blank=True, max_length=100, null=True)),
                ('microbiology_gram_stain_result', models.CharField(blank=True, max_length=100, null=True)),
                ('microbiology_culture_result', models.CharField(blank=True, max_length=100, null=True)),
                ('chemistry_serum_electrolytes_result', models.CharField(blank=True, max_length=100, null=True)),
                ('chemistry_serum_urea_result', models.CharField(blank=True, max_length=100, null=True)),
                ('chemistry_serum_creatinine_result', models.CharField(blank=True, max_length=100, null=True)),
                ('chemistry_urinalysis_result', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('neonate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.newbornadmission')),
            ],
        ),
        migrations.AddField(
            model_name='countymunicipality',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.district'),
        ),
        migrations.CreateModel(
            name='AntenatalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('number_of_times_attended', models.PositiveIntegerField(default=0)),
                ('attended_where', models.CharField(choices=[('Hospital', 'Hospital'), ('Health Centre', 'Health Centre'), ('Private Clinic', 'Private Clinic')], max_length=20)),
                ('conditions_during_pregnancy', models.CharField(choices=[('Diabetes', 'Diabetes'), ('HTN', 'HTN'), ('Pre-eclampsia', 'Pre-eclampsia'), ('APH', 'APH'), ('Malaria', 'Malaria'), ('Uneventful', 'Uneventful'), ('Other', 'Other')], max_length=20)),
                ('received_tetanus_toxoid', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('screened_for_syphilis', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('received_fansidar', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newborn.motherdetails')),
            ],
        ),
    ]
