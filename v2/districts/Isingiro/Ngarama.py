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

    # Create County/Municipality - Bukanga
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Bukanga')

    # Create Subcounty/Town Council/Division - Ngarama
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Ngarama')

    # Create Parish - Ngarama
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Ngarama')

    # Create Villages for Ngarama
    villages_ngarama = ['Kiguri', 'Kimuri', 'Kishojo', 'Kigando', 'Kayenje', 'Kakarakare', 'Katyazo', 'Kyakashana',
                        'Nyanongo', 'Rugorogoro', 'Ruhiira', 'Rwabaganga', 'Rwakabano', 'Rukono']
    for village_name in villages_ngarama:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Kagaaga
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kagaaga')

    # Create Villages for Kagaaga
    villages_kagaaga = ['Bukore', 'Katungamo', 'Rwenshekye east', 'Rwenshekye west', 'Kyandera', 'Kagaaga a', 'Kagaaga b', 'Rumeya']
    for village_name in villages_kagaaga:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Create Parish - Kabaare
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kabaare')

    # Create Villages for Kabaare
    villages_kabaare = ['Biharwe', 'Bushenyi', 'Ishozi', 'Kabaare', 'Kyajungu', 'Karerema', 'Kyamburara', 'Kamutinda',
                        'Mitooma', 'Rugando', 'Ngando']
    for village_name in villages_kabaare:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Create Parish - Burungamo
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Burungamo')

    # Create Villages for Burungamo
    villages_burungamo = ['Bizeera', 'Kibengo i', 'Kibengo ii', 'Rwebinyatsi', 'Rwobuyangaza', 'Kyakabindi central',
                          'Kyakabindi east', 'Kyakabindi north', 'Kyakabindi south', 'Kyakabindi west', 'Kyakayanda',
                          'Rwakabwohe']
    for village_name in villages_burungamo:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

if __name__ == '__main__':
    populate_database()