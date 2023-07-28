# Generated by Django 4.2.2 on 2023-07-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newborn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MothersAntenatalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('number_attended', models.PositiveIntegerField(blank=True, null=True)),
                ('attended_from', models.CharField(blank=True, choices=[('Hospital', 'Hospital'), ('Health Centre', 'Health Centre'), ('Private Clinic', 'Private Clinic')], max_length=50, null=True)),
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
            ],
        ),
    ]
