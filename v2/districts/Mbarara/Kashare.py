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
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Kashari north')

    # Create Subcounty
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Kashare')

    # Create Parish and Villages - Mitoozo
    parish1 = Parish.objects.create(subcounty=subcounty, name='Mitoozo')
    village1 = Village.objects.create(parish=parish1, name='Kitongore')
    village2 = Village.objects.create(parish=parish1, name='Rwembabi i')
    village3 = Village.objects.create(parish=parish1, name='Rwembabi iia')
    village4 = Village.objects.create(parish=parish1, name='Rwembabi iib')
    village5 = Village.objects.create(parish=parish1, name='Kahingo')
    village6 = Village.objects.create(parish=parish1, name='Rwemondo')
    village7 = Village.objects.create(parish=parish1, name='Kyakabano')
    village8 = Village.objects.create(parish=parish1, name='Rwobugoigo')
    village9 = Village.objects.create(parish=parish1, name='Kanaama i')
    village10 = Village.objects.create(parish=parish1, name='Kanaama ii')
    village11 = Village.objects.create(parish=parish1, name='Rwamukondo')
    village12 = Village.objects.create(parish=parish1, name='Ntungamo')

    # Create Parish and Villages - Mirongo
    parish2 = Parish.objects.create(subcounty=subcounty, name='Mirongo')
    village13 = Village.objects.create(parish=parish2, name='Akariza')
    village14 = Village.objects.create(parish=parish2, name='Akabaare')
    village15 = Village.objects.create(parish=parish2, name='Igwanjura')
    village16 = Village.objects.create(parish=parish2, name='Kitsinda')
    village17 = Village.objects.create(parish=parish2, name='Nyamirima')
    village18 = Village.objects.create(parish=parish2, name='Rweibaare i')
    village19 = Village.objects.create(parish=parish2, name='Rweibare ii')
    village20 = Village.objects.create(parish=parish2, name='Rweibare iii')
    village21 = Village.objects.create(parish=parish2, name='Rwencwera i')
    village22 = Village.objects.create(parish=parish2, name='Rwencwera ii')
    village23 = Village.objects.create(parish=parish2, name='Kashare i')
    village24 = Village.objects.create(parish=parish2, name='Kashare ii')
    village25 = Village.objects.create(parish=parish2, name='Mirongo i')
    village26 = Village.objects.create(parish=parish2, name='Mirongo ii')
    village27 = Village.objects.create(parish=parish2, name='Mirongo iii')
    village28 = Village.objects.create(parish=parish2, name='Mirongo iv')
    village29 = Village.objects.create(parish=parish2, name='Mirongo v')

    # Create Parish and Villages - Nchune
    parish3 = Parish.objects.create(subcounty=subcounty, name='Nchune')
    village30 = Village.objects.create(parish=parish3, name='Kyenjojo a')
    village31 = Village.objects.create(parish=parish3, name='Kyenjojo b')
    village32 = Village.objects.create(parish=parish3, name='Nchune a')
    village33 = Village.objects.create(parish=parish3, name='Nchune b')
    village34 = Village.objects.create(parish=parish3, name='Nchune central')
    village35 = Village.objects.create(parish=parish3, name='Nchune iii')
    village36 = Village.objects.create(parish=parish3, name='Nchune kiira')
    village37 = Village.objects.create(parish=parish3, name='Nchune kuryagye')
    village38 = Village.objects.create(parish=parish3, name='Nchune mutima murungi')
    village39 = Village.objects.create(parish=parish3, name='Rugarura')
    village40 = Village.objects.create(parish=parish3, name='Nombe ia')
    village41 = Village.objects.create(parish=parish3, name='Nombe ib')
    village42 = Village.objects.create(parish=parish3, name='Nombe iia')
    village43 = Village.objects.create(parish=parish3, name='Nombe iib')
    village44 = Village.objects.create(parish=parish3, name='Nombe iii')

    # Create Parish and Villages - Nyabisirira
    parish4 = Parish.objects.create(subcounty=subcounty, name='Nyabisirira')
    village45 = Village.objects.create(parish=parish4, name='Akaihamba i')
    village46 = Village.objects.create(parish=parish4, name='Akaihamba ii')
    village47 = Village.objects.create(parish=parish4, name='Akaihamba iii')
    village48 = Village.objects.create(parish=parish4, name='Akaihamba iv')
    village49 = Village.objects.create(parish=parish4, name='Akaihamba v')
    village50 = Village.objects.create(parish=parish4, name='Amabaare east')
    village51 = Village.objects.create(parish=parish4, name='Amabaare west')
    village52 = Village.objects.create(parish=parish4, name='Amabare central')
    village53 = Village.objects.create(parish=parish4, name='Bunyangabo')
    village54 = Village.objects.create(parish=parish4, name='Butaturwa')
    village55 = Village.objects.create(parish=parish4, name='Kyarwanjara')
    village56 = Village.objects.create(parish=parish4, name='Kyenshama')
    village57 = Village.objects.create(parish=parish4, name='Mushabwa')
    village58 = Village.objects.create(parish=parish4, name='Rugarura i')
    village59 = Village.objects.create(parish=parish4, name='Rugarura ii')
    village60 = Village.objects.create(parish=parish4, name='Rugarura iii')
    village61 = Village.objects.create(parish=parish4, name='Rugarura iv')
    village62 = Village.objects.create(parish=parish4, name='Omukabaare i')
    village63 = Village.objects.create(parish=parish4, name='Omukabaare ii')
    village64 = Village.objects.create(parish=parish4, name='Nyabisirira i')
    village65 = Village.objects.create(parish=parish4, name='Nyabisirira ii')

if __name__ == '__main__':
    populate_database()
