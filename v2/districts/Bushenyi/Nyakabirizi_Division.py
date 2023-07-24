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
    # Create District - Bushenyi
    district, _ = District.objects.get_or_create(name='Bushenyi')

    # Create County/Municipality - Bushenyi-ishaka municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Bushenyi-ishaka municipality')

    # Create Subcounty - Nyakabirizi division
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Nyakabirizi division')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Ward i', ['Katungu', 'Nyakabirizi', 'Nshozi']),
        ('Rwenjeru ward', ['Rwenjeru central', 'Rwenjeru t.c', 'Kyanamira', 'Muhiire a', 'Muhiire b', 'Matyazo/masyoro', 'Nshenga a', 'Nshenga b']),
        ('Kibaare ward', ['Igorora', 'Irembezi', 'Bweranyangi a', 'Bweranyangi b', 'Kibaare a', 'Kibaare c', 'Rwemigorora', 'Nyamiko', 'Mazinga', 'Rwakanyonyi', 'Nyakahita a', 'Nyakahita b']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()