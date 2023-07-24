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

    # Create Subcounty - Nyabubare
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Nyabubare')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Nyarugote', ['Kabatura', 'Rwekitooma', 'Kahija i', 'Kahija ii', 'Matiigi', 'Nyakahandagazi', 'Orubingo', 'Nyarugote']),
        ('Nyabubare', ['Bugomora', 'Kibitsya', 'Kyabitara', 'Kashozi', 'Kankinga', 'Matimba', 'Nyabubare', 'Rugaga', 'Rugooma', 'Ruharo', 'Nkuna i', 'Nkuna ii', 'Nyakashebeya', 'Nyabitote i', 'Nyabitote ii', 'Nyarutooma']),
        ('Nkanga', ['Birimbi', 'Kabande a', 'Kabande b', 'Bwera', 'Kibingo', 'Nyamirembe i', 'Nyamirembe ii', 'Kanyegyero', 'Nyamitozo', 'Karondo', 'Nyakashojwa b', 'Nyakatete', 'Nyakatigunda', 'Nkanga', 'Nyakabirizi', 'Oruruku', 'Nyakashojwa a']),
        ('Kizinda', ['Birimbi', 'Bukumbya', 'Kizinda t.c', 'Kibingo', 'Kitooma', 'Katookye', 'Kagati', 'Matsya', 'Rwakaringura', 'Nyakinengo', 'Ntaza']),
        ('Kigoma', ['Bucuma', 'Kirera', 'Kibatsi', 'Kigoma', 'Kigoma t/c', 'Katoma', 'Ryabugahi', 'Kakoma', 'Kambuzi', 'Nyamiko', 'Rwancunda', 'Ncwera', 'Rushoroza']),
        ('Kahungye', ['Bubaare', 'Bukuba i', 'Bukuba ii', 'Kiyagara i', 'Kiyagara ii', 'Kiyagara iii', 'Kitojo i', 'Kitojo ii', 'Kahungye i', 'Kahungye ii', 'Nyakatooma', 'Nyakibingo', 'Oruhita', 'Nyungu i', 'Nyungu ii']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()