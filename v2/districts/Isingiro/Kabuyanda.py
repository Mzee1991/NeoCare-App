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

    # Create Subcounty/Town Council/Division - Kabuyanda
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kabuyanda')

    # Create Parishes and Villages

    parishes = [
        ('Rwakakwenda', ['Akatooma', 'Buteraniro', 'Itaare', 'Katooma', 'Karwenyi', 'Kasharira', 'Rukiiri', 'Rwakakwenda', 'Rutooma', 'Nyaruhanga']),
        ('Kagara', ['Bwengyerere', 'Kyamazinga i', 'Kyamazinga ii', 'Kagara i', 'Kagara ii', 'Rubagano']),
        ('Kabugu', ['Kabeshekyere', 'Kigabagaba i', 'Kigabagaba ii', 'Ekisinga', 'Rwemango', 'Rwedongo', 'Kabugu i', 'Kabugu ii', 'Mishoroshozi', 'Paragoni']),
        ('Kanywamaizi', ['Kagoto i', 'Kagoto ii', 'Nyamiyaga', 'Kanywamaizi i', 'Kanywamaizi ii', 'Kanywamaizi iii', 'Kanywamaizi iv', 'Muhanga', 'Rwabyemera']),
    ]

    for parish_name, village_names in parishes:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()