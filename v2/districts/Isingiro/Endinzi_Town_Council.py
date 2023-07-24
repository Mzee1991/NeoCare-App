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
    # Create District
    district, _ = District.objects.get_or_create(name='Isingiro')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Bukanga')

    # Create Subcounty
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Endinzi town council')

    # Create Parish - Endiinzi town board
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Endiinzi town board')

    # Create Villages for Endiinzi town board
    villages_endiinzi_town_board = [
        ('Endiinzi a'), ('Endiinzi b'), ('Kyarugaju a'),
        ('Kyarugaju b'), ('Kyarugaju c'), ('Nyakakoni')
    ]
    for village_name in villages_endiinzi_town_board:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Endiinzi
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Endiinzi')

    # Create Villages for Endiinzi
    villages_endiinzi = [
        ('Birezi'), ('Engorora'), ('Saano a'), ('Saano b'), ('Orubare')
    ]
    for village_name in villages_endiinzi:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

if __name__ == '__main__':
    populate_database()