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
    # Create District - Kiruhura
    district, _ = District.objects.get_or_create(name='Kiruhura')

    # Create County/Municipality - Kazo
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Kazo')

    # Create Subcounty - Burunga
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Burunga')

    # Create Parishes and Villages for each parish

    # Parishes and Villages as tuples and lists
    parishes_and_villages = [
        ('Rwigi', ['Akembogo', 'Kishongoza', 'Byabasiita', 'Kanyaburezi', 'Rwiigi', 'Kyenshama']),
        ('Kiguma', ['Burama k', 'Bwantama', 'Kiguma', 'Kihwa', 'Kishebashebe', 'Kibani', 'Kyenjoki', 'Muzirangata', 'Mwitanungi']),
        ('Magondo', ['Bisyoro', 'Buhembe', 'Ijwara', 'Kabagore', 'Kabimba', 'Kenwa', 'Kikanja', 'Kidaama', 'Rweibugumya', 'Rwomumbu', 'Magondo', 'Rwabiheera i', 'Rwabiheera ii']),
        ('Burunga', ['Burama b', 'Burunga', 'Buyaga', 'Kiringa', 'Kishororwa', 'Kawiri', 'Kakinga', 'Kyamashita', 'Kampara', 'Mishenyi', 'Rushamaitu']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()