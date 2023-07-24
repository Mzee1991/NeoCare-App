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

    # Create Subcounty
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Rugando')

    # Create Parish and Villages - Nyarubungo
    parish1 = Parish.objects.create(subcounty=subcounty, name='Nyarubungo')
    village1 = Village.objects.create(parish=parish1, name='Buhihi')
    village2 = Village.objects.create(parish=parish1, name='Kyabashukura')
    village3 = Village.objects.create(parish=parish1, name='Kitwe')
    village4 = Village.objects.create(parish=parish1, name='Kakitanga')
    village5 = Village.objects.create(parish=parish1, name='Rwenshama')
    village6 = Village.objects.create(parish=parish1, name='Karora')
    village7 = Village.objects.create(parish=parish1, name='Kagongi')
    village8 = Village.objects.create(parish=parish1, name='Rugarama ii')
    village9 = Village.objects.create(parish=parish1, name='Nyamatete')
    village10 = Village.objects.create(parish=parish1, name='Rurengye')
    village11 = Village.objects.create(parish=parish1, name='Nyakaronko')
    village12 = Village.objects.create(parish=parish1, name='Rubare')
    village13 = Village.objects.create(parish=parish1, name='Nyarubungo')

    # Create Parish and Villages - Mirama
    parish2 = Parish.objects.create(subcounty=subcounty, name='Mirama')
    village14 = Village.objects.create(parish=parish2, name='Kabahesi')
    village15 = Village.objects.create(parish=parish2, name='Kikyerenyo')
    village16 = Village.objects.create(parish=parish2, name='Kisoro')
    village17 = Village.objects.create(parish=parish2, name='Rwemiyenje')
    village18 = Village.objects.create(parish=parish2, name='Rwengiri')
    village19 = Village.objects.create(parish=parish2, name='Rwentobo')
    village20 = Village.objects.create(parish=parish2, name='Mirama i')
    village21 = Village.objects.create(parish=parish2, name='Mirama ii')
    village22 = Village.objects.create(parish=parish2, name='Rubanga')

    # Create Parish and Villages - Nyakabaare
    parish3 = Parish.objects.create(subcounty=subcounty, name='Nyakabaare')
    village23 = Village.objects.create(parish=parish3, name='Buhingo')
    village24 = Village.objects.create(parish=parish3, name='Bukuuna i')
    village25 = Village.objects.create(parish=parish3, name='Bukuuna ii')
    village26 = Village.objects.create(parish=parish3, name='Bushenyi')
    village27 = Village.objects.create(parish=parish3, name='Rwembogo')
    village28 = Village.objects.create(parish=parish3, name='Nyamikanja i')
    village29 = Village.objects.create(parish=parish3, name='Nyamikanja ii')
    village30 = Village.objects.create(parish=parish3, name='Nyakabaare')

    # Create Parish and Villages - Nyabikungu
    parish4 = Parish.objects.create(subcounty=subcounty, name='Nyabikungu')
    village31 = Village.objects.create(parish=parish4, name='Bihendeka')
    village32 = Village.objects.create(parish=parish4, name='Buhama i')
    village33 = Village.objects.create(parish=parish4, name='Buhama ii')
    village34 = Village.objects.create(parish=parish4, name='Butahe')
    village35 = Village.objects.create(parish=parish4, name='Kabobo')
    village36 = Village.objects.create(parish=parish4, name='Kyabaiba')
    village37 = Village.objects.create(parish=parish4, name='Kyabanyoro')
    village38 = Village.objects.create(parish=parish4, name='Enkiri')
    village39 = Village.objects.create(parish=parish4, name='Kasyoro')
    village40 = Village.objects.create(parish=parish4, name='Mikamba')
    village41 = Village.objects.create(parish=parish4, name='Rugarama')
    village42 = Village.objects.create(parish=parish4, name='Nyabikungu')

    # Create Parish and Villages - Kitunguru
    parish5 = Parish.objects.create(subcounty=subcounty, name='Kitunguru')
    village43 = Village.objects.create(parish=parish5, name='Bikonoka')
    village44 = Village.objects.create(parish=parish5, name='Ihunga')
    village45 = Village.objects.create(parish=parish5, name='Kihonzi')
    village46 = Village.objects.create(parish=parish5, name='Kinoni central')
    village47 = Village.objects.create(parish=parish5, name='Kitunguru')
    village48 = Village.objects.create(parish=parish5, name='Katereza')
    village49 = Village.objects.create(parish=parish5, name='Kyabwihure')
    village50 = Village.objects.create(parish=parish5, name='Kyakahira')
    village51 = Village.objects.create(parish=parish5, name='Kyamugasha')
    village52 = Village.objects.create(parish=parish5, name='Nyakaguruka')
    village53 = Village.objects.create(parish=parish5, name='Runena')

if __name__ == '__main__':
    populate_database()
