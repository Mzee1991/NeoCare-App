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

    # Create County/Municipality - Igara east
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Igara east')

    # Create Subcounty - Kyabugimbi
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kyabugimbi')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Kitwe', ['Buhimba a', 'Buhimba b', 'Kitwe central', 'Kitwe-rutooma', 'Rwembirizi', 'Nyamitanga', 'Katunguru', 'Kyakayanga', 'Rutooma a', 'Rutooma b', 'Rutooma central']),
        ('Kyeigombe', ['Kabaare', 'Kibona a', 'Kibona b', 'Nyanga', 'Kyeigombe a', 'Kyeigombe b', 'Kyeigombe c']),
        ('Kajunju', ['Kigimbi', 'Enkombe', 'Kagorogoro', 'Kajunju central', 'Karyango', 'Kyamiko', 'Kyamugasha', 'Kaceeka', 'Mabanga', 'Rugarama']),
        ('Katikamwe', ['Bugarama a', 'Bugarama b', 'Katikamwe a', 'Katikamwe b', 'Rwembirizi', 'Nyamitanga', 'Kyabugimbi tc', 'Kyamutiganzi a', 'Kyamutiganzi b', 'Kyamutiganzi c', 'Kyamutiganzi d', 'Kacence', 'Nyamabare a i', 'Nyamabare a ii', 'Nyamabare b', 'Nyamabare c', 'Nyamabare d']),
        ('Bijengye', ['Bijengye a', 'Bijengye b', 'Bujaga a', 'Bujaga b', 'Kihire', 'Kabura', 'Kyarihigiika', 'Nyakabanga a', 'Nyakabanga b']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()