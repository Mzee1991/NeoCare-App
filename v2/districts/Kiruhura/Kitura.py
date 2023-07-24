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
    district, _ = District.objects.get_or_create(name='Isingiro')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Isingiro north')

    # Create Subcounty
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Ruborogota')

    # Create Parishes and Villages
    parishes = [
        ('Rwangunga', ['Bibungo', 'Ibinja ii', 'Kahororo', 'Katunguru', 'Kagabagaba', 'Rwangunga']),
        ('Ruborogota', ['Kabatangare', 'Kibabo', 'Mpoma i', 'Mpoma ii', 'Ruborogota i']),
        ('Nshenyi', ['Bugarika', 'Kagera', 'Nyabugando', 'Nshenyi']),
        ('Kyamusoni', ['Kihihi', 'Kahama', 'Kyamusoni', 'Kabumba', 'Kagando', 'Ruzinga', 'Rukureijo']),
        ('Karama', ['Ibinja i', 'Kibingo i', 'Kibingo ii', 'Kigando', 'Karama i', 'Karama ii', 'Kagarama'])
    ]

    for parish_name, village_names in parishes:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        create_villages(parish, village_names)

if __name__ == '__main__':
    populate_database()