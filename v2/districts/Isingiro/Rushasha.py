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
    # Create District
    district, _ = District.objects.get_or_create(name='Isingiro')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Bukanga')

    # Create Subcounty - Rushasha
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Rushasha')

    # Create Parish - Rwantaha
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Rwantaha')

    # Create Villages for Rwantaha
    villages_rwantaha = ['Kyabuzare', 'Rwantaha a', 'Rwantaha b', 'Rwantaha c', 'Rwabarimirizi a', 'Rwabarimirizi b', 'Nyungu']
    for village_name in villages_rwantaha:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Rushasha
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Rushasha')

    # Create Villages for Rushasha
    villages_rushasha = ['Ekirinda', 'Nyanga', 'Karunga', 'Kamutiganzi', 'Ndayanjojo', 'Rushasha']
    for village_name in villages_rushasha:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Create Parish - Mirambiro
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Mirambiro')

    # Create Villages for Mirambiro
    villages_mirambiro = ['Kabahara', 'Kabazana', 'Kiyenje', 'Kashasha', 'Kabwera', 'Misyera', 'Ruhooko a', 'Ruhooko b']
    for village_name in villages_mirambiro:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Create Parish - Ihunga
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Ihunga')

    # Create Villages for Ihunga
    villages_ihunga = ['Kendobo', 'Kinami', 'Kisuura', 'Kyembogo', 'Rubingo']
    for village_name in villages_ihunga:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

if __name__ == '__main__':
    populate_database()