# Generated by Django 4.2.2 on 2023-10-16 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newborn', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('other_names', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('religion', models.CharField(choices=[('Catholic', 'Catholic'), ('Anglican', 'Anglican'), ('Muslim', 'Muslim'), ('Seventh Day Adventist', 'Seventh Day Adventist'), ('Orthodox', 'Orthodox'), ('Pentecostal', 'Pentecostal'), ('Others', 'Others')], max_length=50)),
                ('tribe', models.CharField(max_length=50)),
                ('next_of_kin', models.CharField(max_length=100)),
                ('relationship', models.CharField(choices=[('Mother', 'Mother'), ('Father', 'Father'), ('Aunt', 'Aunt'), ('Uncle', 'Uncle'), ('Grandfather', 'Grandfather'), ('Grandmother', 'Grandmother'), ('Guardian', 'Guardian'), ('Other Relative', 'Other Relative')], max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newborn.motherlocation')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
