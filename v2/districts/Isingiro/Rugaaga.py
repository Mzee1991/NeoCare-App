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

    # Create Subcounty - Rugaaga
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Rugaaga')

    # Create Parish - Rwangabo
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Rwangabo')

    # Create Villages for Rwangabo
    villages_rwangabo = [
        'Keibarye', 'Kiiju', 'Kemengo', 'Kahima', 'Katooma', 'Kaitagura',
        'Rwendezi', 'Kyamugasha', 'Kagando a', 'Kagando b', 'Rwangabo a',
        'Rwangabo b', 'Ntungamo', 'Nyaruhuzi a', 'Nyaruhuzi b'
    ]
    for village_name in villages_rwangabo:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Nyabubaare
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Nyabubaare')

    # Create Villages for Nyabubaare
    villages_nyabubaare = [
        'Kijubwe', 'Kigazi', 'Rwembeba', 'Katuntu', 'Rwenturagara', 'Kashare',
        'Rutunga', 'Nyabubaare'
    ]
    for village_name in villages_nyabubaare:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Create Parish - Kiryaburo
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kiryaburo')

    # Create Villages for Kiryaburo
    villages_kiryaburo = [
        'Bururuma i', 'Bururuma ii', 'Kabaare', 'Kiryaburo a', 'Kiryaburo b',
        'Rwankakire', 'Rwakinono'
    ]
    for village_name in villages_kiryaburo:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Create Parish - Kyarubambura
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kyarubambura')

    # Create Villages for Kyarubambura
    villages_kyarubambura = [
        'Birunduma', 'Kitooma (Selected Village)', 'Katokye', 'Rwenturagara',
        'Kyamutura', 'Kabuhembe', 'Kashambya', 'Rukuuba'
    ]
    for village_name in villages_kyarubambura:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

    # Create Parish - Kyampango
    parish5, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kyampango')

    # Create Villages for Kyampango
    villages_kyampango = [
        'Keikobe', 'Kahega', 'Kakiika', 'Kyampango a', 'Kyampango b', 'Kyanyanda',
        'Kanikwa', 'Rugaaga', 'Ndayiga', 'Nyakaziba'
    ]
    for village_name in villages_kyampango:
        village, _ = Village.objects.get_or_create(parish=parish5, name=village_name)

    # Create Parish - Kabaare
    parish6, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kabaare')

    # Create Villages for Kabaare
    villages_kabaare = [
        'Kabare i', 'Kabare ii', 'Kikunyu a', 'Kikunyu b', 'Kajumbura',
        'Nyamiyonga', 'Kashenyi', 'Kafumba', 'Ruhanga'
    ]
    for village_name in villages_kabaare:
        village, _ = Village.objects.get_or_create(parish=parish6, name=village_name)

    # Create Parish - Kashojwa
    parish7, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kashojwa')

    # Create Villages for Kashojwa
    villages_kashojwa = [
        'Kazuura', 'Kiretwa', 'Karokarungi', 'Kashojwa', 'Kashwina a', 'Kashwina b'
    ]
    for village_name in villages_kashojwa:
        village, _ = Village.objects.get_or_create(parish=parish7, name=village_name)

if __name__ == '__main__':
    populate_database()