# Generated by Django 4.2.2 on 2023-06-21 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newborn', '0001_initial'),
    ]

    operations = [
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
