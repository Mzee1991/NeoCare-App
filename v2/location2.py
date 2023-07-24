#!/usr/bin/python3


import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from newborn.models import District, Subcounty, Parish, Village, CountyMunicipality

def populate_database():
    # Create District
    district = District.objects.create(name='Mbarara')

    # Create County/Municipality
    county_municipality = CountyMunicipality.objects.create(district=district, name='Mbarara municipality')

    # Create Subcounty
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Nyamitanga')

    # Create Parish
    parish = Parish.objects.create(subcounty=subcounty, name='Katete')

    # Create Villages
    village1 = Village.objects.create(parish=parish, name='Bihunya')
    village2 = Village.objects.create(parish=parish, name='Kitebero')
    village3 = Village.objects.create(parish=parish, name='Katete central')
    village4 = Village.objects.create(parish=parish, name='Nyamitanga')
    village5 = Village.objects.create(parish=parish, name='Rwemirinzi')
    village6 = Village.objects.create(parish=parish, name='Karugangama')
    village7 = Village.objects.create(parish=parish, name='Rwizi')
    village8 = Village.objects.create(parish=parish, name='Nsikye')

if __name__ == '__main__':
    populate_database()
