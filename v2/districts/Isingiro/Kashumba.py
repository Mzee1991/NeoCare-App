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

    # Create Subcounty - Kashumba
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kashumba')

    # Create Parish - Rushwa
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Rushwa')

    # Create Villages for Rushwa
    villages_rushwa = [
        'Kiyenje', 'Rwenjeru', 'Katyazo', 'Kyabibabi', 'Rwamacumu a',
        'Rwamacumu b', 'Nyakabingo a', 'Nyakabingo b', 'Rushwa', 'Ntungamo'
    ]
    for village_name in villages_rushwa:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Murema
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Murema')

    # Create Villages for Murema
    villages_murema = [
        'Kigando', 'Kiterede', 'Kabura ii', 'Murema a', 'Murema b', 'Murema central'
    ]
    for village_name in villages_murema:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Create Parish - Kigaragara
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kigaragara')

    # Create Villages for Kigaragara
    villages_kigaragara = [
        'Bushungwe', 'Kitanda', 'Kigaragara a', 'Kigaragara b', 'Kyakahura', 'Karora a',
        'Karora b', 'Kamishwa', 'Kasheshe', 'Kagaara', 'Ntenga a', 'Ntenga b', 'Ntenga c'
    ]
    for village_name in villages_kigaragara:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Create Parish - Kashumba
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kashumba')

    # Create Villages for Kashumba
    villages_kashumba = [
        'Burama', 'Byenyi', 'Kashumba', 'Kagango', 'Rubare', 'Rubombo', 'Nyaruti'
    ]
    for village_name in villages_kashumba:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

    # Create Parish - Kasharira
    parish5, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kasharira')

    # Create Villages for Kasharira
    villages_kasharira = [
        'Kiriima', 'Keminazi', 'Kabura i', 'Kasharira', 'Rumuri'
    ]
    for village_name in villages_kasharira:
        village, _ = Village.objects.get_or_create(parish=parish5, name=village_name)

    # Create Parish - Kankingi
    parish6, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kankingi')

    # Create Villages for Kankingi
    villages_kankingi = [
        'Juru', 'Kabatamba', 'Kabirizi', 'Kazya', 'Kityaza', 'Kashojwa', 'Kankingi', 'Rukinga'
    ]
    for village_name in villages_kankingi:
        village, _ = Village.objects.get_or_create(parish=parish6, name=village_name)

if __name__ == '__main__':
    populate_database()