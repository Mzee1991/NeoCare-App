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
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Rwampara')

    # Create Subcounty - Ndeija
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Ndeija')

    # Create Parish - Bujaga
    parish1 = Parish.objects.create(subcounty=subcounty, name='Bujaga')
    village1 = Village.objects.create(parish=parish1, name='Bujaga a')
    village2 = Village.objects.create(parish=parish1, name='Bujaga b')
    village3 = Village.objects.create(parish=parish1, name='Bujaga central')
    village4 = Village.objects.create(parish=parish1, name='Buteraniro east')
    village5 = Village.objects.create(parish=parish1, name='Buteraniro west')
    village6 = Village.objects.create(parish=parish1, name='Kijojo a')
    village7 = Village.objects.create(parish=parish1, name='Kashuro')
    village8 = Village.objects.create(parish=parish1, name='Nyakahanga')

    # Create Parish - Kakigani
    parish2 = Parish.objects.create(subcounty=subcounty, name='Kakigani')
    village9 = Village.objects.create(parish=parish2, name='Biiti')
    village10 = Village.objects.create(parish=parish2, name='Kitete')
    village11 = Village.objects.create(parish=parish2, name='Kitookye')
    village12 = Village.objects.create(parish=parish2, name='Kanyangi')
    village13 = Village.objects.create(parish=parish2, name='Karagwe')
    village14 = Village.objects.create(parish=parish2, name='Kacucu')
    village15 = Village.objects.create(parish=parish2, name='Rugarama')
    village16 = Village.objects.create(parish=parish2, name='Rutooma')
    village17 = Village.objects.create(parish=parish2, name='Town cell')
    village18 = Village.objects.create(parish=parish2, name='Nyarutuutu')

    # Create Parish - Kibare
    parish3 = Parish.objects.create(subcounty=subcounty, name='Kibare')
    village19 = Village.objects.create(parish=parish3, name='Ihena')
    village20 = Village.objects.create(parish=parish3, name='Kiziba')
    village21 = Village.objects.create(parish=parish3, name='Kibaare')
    village22 = Village.objects.create(parish=parish3, name='Kibumba')
    village23 = Village.objects.create(parish=parish3, name='Kakuuto')
    village24 = Village.objects.create(parish=parish3, name='Murago')

    # Create Parish - Kongoro
    parish4 = Parish.objects.create(subcounty=subcounty, name='Kongoro')
    village25 = Village.objects.create(parish=parish4, name='Buyonga')
    village26 = Village.objects.create(parish=parish4, name='Kongoro')
    village27 = Village.objects.create(parish=parish4, name='Kyancere')
    village28 = Village.objects.create(parish=parish4, name='Kyeiremba')
    village29 = Village.objects.create(parish=parish4, name='Rugazi')

    # Create Parish - Ndeija-mulago
    parish5 = Parish.objects.create(subcounty=subcounty, name='Ndeija-mulago')
    village30 = Village.objects.create(parish=parish5, name='Ibaare')
    village31 = Village.objects.create(parish=parish5, name='Kashuro')
    village32 = Village.objects.create(parish=parish5, name='Kyesika i')
    village33 = Village.objects.create(parish=parish5, name='Kyesika ii')
    village34 = Village.objects.create(parish=parish5, name='Ndeija i')
    village35 = Village.objects.create(parish=parish5, name='Ndeija ii')
    village36 = Village.objects.create(parish=parish5, name='Nyindo')

    # Create Parish - Nyakaikara
    parish6 = Parish.objects.create(subcounty=subcounty, name='Nyakaikara')
    village37 = Village.objects.create(parish=parish6, name='Kibuba')
    village38 = Village.objects.create(parish=parish6, name='Kigarama')
    village39 = Village.objects.create(parish=parish6, name='Kitojo b')
    village40 = Village.objects.create(parish=parish6, name='Rukono')
    village41 = Village.objects.create(parish=parish6, name='Nyakaikara')

    # Create Parish - Nyeihanga
    parish7 = Parish.objects.create(subcounty=subcounty, name='Nyeihanga')
    village42 = Village.objects.create(parish=parish7, name='Bungyereza')
    village43 = Village.objects.create(parish=parish7, name='Karunyonyozi')
    village44 = Village.objects.create(parish=parish7, name='Kyenombe')
    village45 = Village.objects.create(parish=parish7, name='Rwabajojo')
    village46 = Village.objects.create(parish=parish7, name='Nyamabare')
    village47 = Village.objects.create(parish=parish7, name='Rushasha')
    village48 = Village.objects.create(parish=parish7, name='Nyeihanga')
    village49 = Village.objects.create(parish=parish7, name='Nyeihanga central')
    village50 = Village.objects.create(parish=parish7, name='Nyeihanga t/c')

    # Create Parish - Rwensinga
    parish8 = Parish.objects.create(subcounty=subcounty, name='Rwensinga')
    village51 = Village.objects.create(parish=parish8, name='Akacence')
    village52 = Village.objects.create(parish=parish8, name='Busingye')
    village53 = Village.objects.create(parish=parish8, name='Izinga')
    village54 = Village.objects.create(parish=parish8, name='Rwengwe')
    village55 = Village.objects.create(parish=parish8, name='Kabutare')
    village56 = Village.objects.create(parish=parish8, name='Kacuucu')
    village57 = Village.objects.create(parish=parish8, name='Mutojo')
    village58 = Village.objects.create(parish=parish8, name='Rutoma')
    village59 = Village.objects.create(parish=parish8, name='Nyakabungo')

if __name__ == '__main__':
    populate_database()
