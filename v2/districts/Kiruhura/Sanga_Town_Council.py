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

    # Create Subcounty - Sanga town council
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Sanga town council')

    # Create Parishes and Villages for each parish

    parishes_and_villages = [
        ('Sanga ward', ['Sanga a', 'Sanga b']),
        ('Nombe ward', ['Kibega', 'Kyakanyantsi', 'Rufuka']),
        ('Nkongoro ward', ['Akabaare', 'Nkongoro (ranches 13, 14, 15)', 'Ntuura (ranches 9 & 10)']),
        ('Ekizimbi ward', ['Kakagate', 'Kasharara']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()