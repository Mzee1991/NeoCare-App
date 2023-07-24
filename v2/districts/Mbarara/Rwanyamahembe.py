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
    district, _ = District.objects.get_or_create(name='Mbarara')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Kashari south')

    # Create Subcounty
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Rwanyamahembe')

    # Create Parish and Villages - Rwebishekye
    parish1 = Parish.objects.create(subcounty=subcounty, name='Rwebishekye')
    village1 = Village.objects.create(parish=parish1, name='Kikoma')
    village2 = Village.objects.create(parish=parish1, name='Bwizibwera')
    village3 = Village.objects.create(parish=parish1, name='Bwizibwera t/c b')
    village4 = Village.objects.create(parish=parish1, name='Rwebishekye i')
    village5 = Village.objects.create(parish=parish1, name='Rwebishekye ii')
    village6 = Village.objects.create(parish=parish1, name='Kabureishokye')
    village7 = Village.objects.create(parish=parish1, name='Muko')
    village8 = Village.objects.create(parish=parish1, name='Mushenyi')

    # Create Parish and Villages - Rutoma
    parish2 = Parish.objects.create(subcounty=subcounty, name='Rutoma')
    village9 = Village.objects.create(parish=parish2, name='Bugarama')
    village10 = Village.objects.create(parish=parish2, name='Butagatsi')
    village11 = Village.objects.create(parish=parish2, name='Ihanika i')
    village12 = Village.objects.create(parish=parish2, name='Ihanika ii')
    village13 = Village.objects.create(parish=parish2, name='Kishunju i')
    village14 = Village.objects.create(parish=parish2, name='Kishunju ii')
    village15 = Village.objects.create(parish=parish2, name='Rwampara')
    village16 = Village.objects.create(parish=parish2, name='Rutooma')
    village17 = Village.objects.create(parish=parish2, name='Rutooma t/c')
    village18 = Village.objects.create(parish=parish2, name='Ogwengoma')

    # Create Parish and Villages - Mabira
    parish3 = Parish.objects.create(subcounty=subcounty, name='Mabira')
    village19 = Village.objects.create(parish=parish3, name='Kitookye')
    village20 = Village.objects.create(parish=parish3, name='Kyagaju')
    village21 = Village.objects.create(parish=parish3, name='Kacwamba')
    village22 = Village.objects.create(parish=parish3, name='Mabira')
    village23 = Village.objects.create(parish=parish3, name='Rugarama')
    village24 = Village.objects.create(parish=parish3, name='Orubare')

    # Create Parish and Villages - Kakyerere
    parish4 = Parish.objects.create(subcounty=subcounty, name='Kakyerere')
    village25 = Village.objects.create(parish=parish4, name='Bwizibwera t/c')
    village26 = Village.objects.create(parish=parish4, name='Rweishaka')
    village27 = Village.objects.create(parish=parish4, name='Kakyerere')
    village28 = Village.objects.create(parish=parish4, name='Karuyenje a')
    village29 = Village.objects.create(parish=parish4, name='Karuyenje b')
    village30 = Village.objects.create(parish=parish4, name='Rwanyamahembe')
    village31 = Village.objects.create(parish=parish4, name='Nyakayojo a')
    village32 = Village.objects.create(parish=parish4, name='Nyakayojo b')
    village33 = Village.objects.create(parish=parish4, name='Rutooma')

    # Create Parish and Villages - Katyazo
    parish5 = Parish.objects.create(subcounty=subcounty, name='Katyazo')
    village34 = Village.objects.create(parish=parish5, name='Rweishamiro')
    village35 = Village.objects.create(parish=parish5, name='Katyazo')
    village36 = Village.objects.create(parish=parish5, name='Kyakaziizi')
    village37 = Village.objects.create(parish=parish5, name='Karukushu')
    village38 = Village.objects.create(parish=parish5, name='Karwondo')
    village39 = Village.objects.create(parish=parish5, name='Rwentojo')
    village40 = Village.objects.create(parish=parish5, name='Kyeshamire')
    village41 = Village.objects.create(parish=parish5, name='Nyabugando')
    village42 = Village.objects.create(parish=parish5, name='Nyakazinga')
    village43 = Village.objects.create(parish=parish5, name='Runengo')

if __name__ == '__main__':
    populate_database()
