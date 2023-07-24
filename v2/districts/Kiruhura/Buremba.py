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

def create_villages(parish, village_names):
    for village_name in village_names:
        village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

def populate_database():
    # Create District
    district, _ = District.objects.get_or_create(name='Kiruhura')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Kazo')

    # Create Subcounty
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Buremba')

    # Create Parishes and Villages
    parishes = [
        ('Ngomba', ['Kagando', 'Rwamanyonyi i', 'Rwamanyonyi ii', 'Mataaba i', 'Mataaba ii', 'Ngomba', 'Rushango ii']),
        ('Kyabahura', ['Bwantaama', 'Kyabahura i', 'Kyabahura ii', 'Kakoma', 'Mirambi', 'Mukunguru i', 'Mukunguru ii', 'Mukunguru iii']),
        ('Kitamba', ['Bujwakwezi', 'Kitamba i', 'Kitamba ii', 'Kitooma', 'Katunguru', 'Ryensindizi', 'Nsinungi']),
        ('Kijooha', ['Buremba', 'Buremba central', 'Kijooha', 'Bwizi a', 'Katongore', 'Rwengwe', 'Karebe', 'Mishambya']),
        ('Kakoni', ['Kakoni a', 'Kakoni b', 'Marumba', 'Rushango i', 'Ruyubu', 'Omukabare']),
        ('Kabingo', ['Kabingo a', 'Kabingo b', 'Kishororo', 'Kinyugunyu', 'Mpuuga a', 'Mpuuga b', 'Omunzigye']),
        ('Bigutsyo', ['Bigutsyo', 'Bwiizi b', 'Kibwera', 'Kamugyene', 'Kanisya'])
    ]

    for parish_name, village_names in parishes:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        create_villages(parish, village_names)

if __name__ == '__main__':
    populate_database()