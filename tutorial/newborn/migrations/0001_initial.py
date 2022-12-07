# Generated by Django 4.1.3 on 2022-12-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newborn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('admission_date', models.DateField()),
                ('gestation_age', models.IntegerField(default=28)),
                ('diagnosis', models.CharField(max_length=100)),
                ('discharge_date', models.DateField()),
            ],
            options={
                'ordering': ['admission_date'],
            },
        ),
    ]