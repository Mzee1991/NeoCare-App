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

    # Create County/Municipality - Igara west
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Igara west')

    # Create Subcounty - Kyamuhunga
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kyamuhunga')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Swazi', ['Butare', 'Katima', 'Kajugangoma', 'Ryanyamihondo', 'Kyampebwe', 'Omunjeru', 'Swazi i', 'Swazi ii', 'Swazi iii']),
        ('Nshumi', ['Kibatsi', 'Kibingo', 'Kanyabiko', 'Kanyambare', 'Nyampungye', 'Ryamihuga', 'Kyaruhaga', 'Rugarama', 'Nyakabare', 'Rutooma', 'Nshumi', 'Nyakishojwa', 'Orubingo', 'Tekateeka']),
        ('Kakoni', ['Rwenjojo', 'Kakoni', 'Kyeibumba', 'Manengo a', 'Manengo b', 'Nyamashobe']),
        ('Kabingo', ['Bugongo', 'Igara tea factory', 'Butare t/c', 'Kyabajojo', 'Kisingo', 'Bwombere', 'Karire', 'Ryampanga', 'Kyeikamba', 'Rwanshetsya', 'Rubuzagye', 'Nyakatooma', 'Nyakatsiro', 'Nyakahanga a', 'Nyakahanga b', 'Rubaare', 'Nyakashojwa', 'Torotoro']),
        ('Kibazi', ['Kikumbagazo', 'Kibazi', 'Kibona', 'Kayanga', 'Katarimwa', 'Nyakatembe i', 'Nyakatembe ii', 'Nyakazinga']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()