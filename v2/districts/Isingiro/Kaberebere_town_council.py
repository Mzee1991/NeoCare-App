#!/usr/bin/python3

import os
import django
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from newborn.models import District, Subcounty, Parish, Village, CountyMunicipality

def populate_database():
    # Create District - Isingiro
    district, _ = District.objects.get_or_create(name='Isingiro')

    # Create County/Municipality - Isingiro north
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Isingiro north')

    # Create Subcounty/Town Council/Division - Kaberebere town council
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kaberebere town council')

    # Create Parish - Kaberebere east ward
    parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kaberebere east ward')

    # Create Villages for Kaberebere east ward
    villages = [
        'Akateete', 'Kaberebere i', 'Kaberebere ii', 'Kabirizi', 'Kikokwa i', 'Rweiziringiro ii', 'Kyabutooto', 'Kyenyangi', 'Rutsya'
    ]
    for village_name in villages:
        village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()