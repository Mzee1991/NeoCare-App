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

    # Create Subcounty - Bumbaire
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Bumbaire')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Numba', ['Ahanjeru', 'Keijengye', 'Kawaga', 'Katonya', 'Rwenkogote', 'Nyakabirizi', 'Rutooma', 'Nyakahembe', 'Numba central', 'Numba ii', 'Nyaruzinga']),
        ('Kiyaga', ['Bugarama', 'Kiyaga', 'Kihororo', 'Kirundo', 'Kibingo', 'Kigoma', 'Kateramo', 'Rwemirabyo', 'Nyamizi', 'Kyamabare', 'Rwentaka', 'Kantunda', 'Nyamiko', 'Nyabwina', 'Obwiho']),
        ('Kibaare', ['Irashaniro', 'Kibare b', 'Katenga', 'Ryanteretere', 'Miiti', 'Maino', 'Nyabubare a', 'Nyabubare b', 'Nyakatugunda']),
        ('Bumbaire ii', ['Bumbaire i', 'Bumbaire ii (selected)', 'Bushanje', 'Kihunda', 'Kitakuka', 'Kitsibo', 'Nyamirima', 'Nyamiyaga', 'Rwencence', 'Nyandozo', 'Kabushaho', 'Kamutazya', 'Kagati', 'Rwamabare', 'Nyakabungo', 'Rwakati']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()