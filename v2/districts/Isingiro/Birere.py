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

    # Create Subcounty/Town Council/Division - Birere
    subcounty1, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Birere')

    # Create Parish - Kishuro
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Kishuro')

    # Create Villages for Kishuro
    villages_kishuro = ['Butenga i', 'Butenga ii', 'Kabaare i', 'Kabaare ii', 'Kishuro', 'Kamakisa', 'Nyabweshongoza']
    for village_name in villages_kishuro:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Kikokwa
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Kikokwa')

    # Create Villages for Kikokwa
    villages_kikokwa = ['Birere', 'Kikokwa ii', 'Rweiziringiro i', 'Mikonoigana', 'Rwakiruri']
    for village_name in villages_kikokwa:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Create Parish - Kyera
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Kyera')

    # Create Villages for Kyera
    villages_kyera = ['Kitooma i', 'Kitooma ii', 'Rwencwera i', 'Rwencwera ii', 'Kashenyi', 'Kyera i', 'Kyera ii']
    for village_name in villages_kyera:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Create Parish - Kahenda
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Kahenda')

    # Create Villages for Kahenda
    villages_kahenda = ['Kitooha', 'Kahenda i', 'Kahenda ii', 'Ndaragi', 'Nsiika', 'Rubeya']
    for village_name in villages_kahenda:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

    # Create Parish - Kasaana
    parish5, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Kasaana')

    # Create Villages for Kasaana
    villages_kasaana = ['Kiboona i', 'Kiboona ii', 'Kasaana i', 'Kasaana ii', 'Mpambazi', 'Rugarama', 'Nyabuziba', 'Rukoma', 'Nyakibare']
    for village_name in villages_kasaana:
        village, _ = Village.objects.get_or_create(parish=parish5, name=village_name)

if __name__ == '__main__':
    populate_database()