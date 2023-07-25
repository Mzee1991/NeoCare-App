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
    # Create District - Ibanda
    district, _ = District.objects.get_or_create(name='Ibanda')

    # Create County/Municipality - Ibanda south
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Ibanda south')

    # Create Subcounty - Keihangara
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Keihangara')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Rwenshambya', ['Bihembe i', 'Bihembe ii', 'Bihembe iii', 'Bihembe iv', 'Rwensambya i', 'Rwensambya ii', 'Rwensambya iii', 'Rwensambya iv', 'Kakunama i', 'Rukinga i', 'Rukinga ii']),
        ('Rugaaga', ['Kajwamushana ii', 'Kajwamushana iii', 'Kajwamushana v', 'Kakunama ii', 'Kakunama iii', 'Kaburo i', 'Kaburo ii', 'Kyenyena', 'Rugaaga i', 'Rugaaga ii', 'Rugaaga iii', 'Rugaaga iv', 'Rugaaga v']),
        ('Keihangara', ['Kabingo', 'Keihangara i', 'Keihangara ii', 'Keihangara iii', 'Keihangara iv', 'Keihangara v', 'Kajwamushana i', 'Kajwamushana iv', 'Rweshebeshebe', 'Kyarukumba i']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()