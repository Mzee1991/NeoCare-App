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

    # Create Subcounty - Mbaare
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Mbaare')

    # Create Parish - Nyamarungi
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Nyamarungi')

    # Create Villages for Nyamarungi
    villages_nyamarungi = [
        'Buhunga i', 'Burunga ii', 'Bwizi', 'Nyamarungi a', 'Nyamarungi b',
        'Nyamarungi central', 'Obugaaga'
    ]
    for village_name in villages_nyamarungi:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Ruteete
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Ruteete')

    # Create Villages for Ruteete
    villages_ruteete = [
        'Bubarebwera', 'Kempara', 'Rwengwe', 'Ruteete a', 'Ruteete b', 'Ruteete c'
    ]
    for village_name in villages_ruteete:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Create Parish - Nshororo
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Nshororo')

    # Create Villages for Nshororo
    villages_nshororo = [
        'Bugango i', 'Bugango ii', 'Bujubwe', 'Kikokwa', 'Kahungye', 'Mbare i',
        'Mbare ii', 'Nshororo'
    ]
    for village_name in villages_nshororo:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Create Parish - Kyabahesi
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kyabahesi')

    # Create Villages for Kyabahesi
    villages_kyabahesi = [
        'Bahiigi a', 'Bahiigi b', 'Kaziizi a', 'Kaziizi b', 'Kikoma', 'Kyabahesi a',
        'Kyabahesi b', 'Katojo central', 'Katojo i', 'Katojo ii', 'Katahooka', 'Rwabahinda'
    ]
    for village_name in villages_kyabahesi:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

    # Create Parish - Kihanda
    parish5, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kihanda')

    # Create Villages for Kihanda
    villages_kihanda = [
        'Ishunga', 'Kihanda central', 'Kirebareba', 'Kibeba', 'Kiviga', 'Rwenshekye',
        'Kasharara a', 'Kasharara b', 'Kyarukorongo', 'Mishenyi a', 'Mishenyi b', 'Rutanga'
    ]
    for village_name in villages_kihanda:
        village, _ = Village.objects.get_or_create(parish=parish5, name=village_name)

    # Create Parish - Burigi
    parish6, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Burigi')

    # Create Villages for Burigi
    villages_burigi = [
        'Bubarebwera', 'Burigi a', 'Burigi central', 'Burigi i', 'Burigi ii', 'Rwenshebasheshe'
    ]
    for village_name in villages_burigi:
        village, _ = Village.objects.get_or_create(parish=parish6, name=village_name)

if __name__ == '__main__':
    populate_database()