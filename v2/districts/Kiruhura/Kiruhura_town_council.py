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
    # Create District - Kiruhura
    district, _ = District.objects.get_or_create(name='Kiruhura')

    # Create County/Municipality - Nyabushozi
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Nyabushozi')

    # Create Subcounty - Kiruhura town council
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kiruhura town council')

    # Create Parishes and Villages for each parish

    parishes_and_villages = [
        ('Nyakasharara', ['Mwaka ii', 'Mwaka iii', 'Nyakasharara']),
        ('Kiruhura ward', ['Kiruhura i', 'Kiruhura ii', 'Kitookye']),
        ('Kashwa ward', ['Kenshunga', 'Karengyezo', 'Kashwa']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()