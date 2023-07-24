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

    # Create Subcounty - Bitooma
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Bitooma')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Nyarugote', ['Bitooma a', 'Bitooma b', 'Bitooma c', 'Bitooma central', 'Kanyamuteera', 'Kashororo']),
        ('Nyanga', ['Bugomora', 'Kabaare', 'Rwengwe', 'Nyanga central', 'Kyamamari', 'Kashasha', 'Nyakarehe']),
        ('Ngorora', ['Kayengo', 'Ryeseera a', 'Ryeseera b', 'Mushakira', 'Rugarama', 'Ngorora']),
        ('Kimuri', ['Kimuri', 'Kyasha', 'Makweteere', 'Murambi', 'Nyabwirima', 'Nyakibaya']),
        ('Kakira', ['Kongo', 'Kagunga', 'Kanyamukundi', 'Kakira', 'Ryamuganga', 'Nyakatembe', 'Nyakashojwa']),
        ('Kashambya', ['Ryakatimbiri', 'Kashambya', 'Kyanyamugiira', 'Rwanziro']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()