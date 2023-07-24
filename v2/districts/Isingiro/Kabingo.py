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

    # Create Subcounty/Town Council/Division - Kabingo
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kabingo')

    # Create Parishes and Villages

    parishes = [
        ('Nyakigyera', ['Burara i', 'Burara ii', 'Bwanga i', 'Bwanga ii', 'Kyebikara', 'Kyempara i', 'Rugaaga', 'Nyakibare', 'Nyakabungo', 'Rushayo']),
        ('Kyeirumba', ['Kabagabe', 'Byaruha i', 'Byaruha ii', 'Kyempara ii', 'Nyabugando', 'Rugara']),
        ('Kyarugaaju', ['Kayonza', 'Kyabwemi', 'Kyarugaju', 'Kyarugamba', 'Kacombeka', 'Kagamba', 'Kagogo', 'Nyakagyera', 'Rubira']),
        ('Kyabinunga', ['Bungura a', 'Bungura b', 'Kitura a', 'Kitura b', 'Kyabinunga a', 'Kyabinunga b', 'Rwanyakihanga', 'Mbaare', 'Rukono']),
        ('Kagarama', ['Amakukuru', 'Kabibi a', 'Kabibi b', 'Keitabikyere', 'Kicwekano', 'Kagarama', 'Muhunga', 'Rugaara', 'Rwakashaka']),
        ('Katembe', ['Bitooma', 'Katembe', 'Katembe central', 'Kataraka', 'Mpororo', 'Rwabashandura']),
    ]

    for parish_name, village_names in parishes:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()