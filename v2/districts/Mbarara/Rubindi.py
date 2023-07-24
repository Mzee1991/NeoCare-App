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
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Rubindi')

    # Create Parish and Villages - Nyamiriro
    parish1 = Parish.objects.create(subcounty=subcounty, name='Nyamiriro')
    village1 = Village.objects.create(parish=parish1, name='Akacence i')
    village2 = Village.objects.create(parish=parish1, name='Bugorora')
    village3 = Village.objects.create(parish=parish1, name='Kabirizi')
    village4 = Village.objects.create(parish=parish1, name='Kizinda')
    village5 = Village.objects.create(parish=parish1, name='Kibwijo')
    village6 = Village.objects.create(parish=parish1, name='Kanyabuye')
    village7 = Village.objects.create(parish=parish1, name='Nyamiriro')
    village8 = Village.objects.create(parish=parish1, name='Kandihere')
    village9 = Village.objects.create(parish=parish1, name='Katagata')
    village10 = Village.objects.create(parish=parish1, name='Katamutoijo')
    village11 = Village.objects.create(parish=parish1, name='Mubanda')
    village12 = Village.objects.create(parish=parish1, name='Mbarama')
    village13 = Village.objects.create(parish=parish1, name='Nyakatookye')
    village14 = Village.objects.create(parish=parish1, name='Rukanja')
    village15 = Village.objects.create(parish=parish1, name='Omugyera')

    # Create Parish and Villages - Rwamuhiigi
    parish2 = Parish.objects.create(subcounty=subcounty, name='Rwamuhiigi')
    village16 = Village.objects.create(parish=parish2, name='Akacence ii')
    village17 = Village.objects.create(parish=parish2, name='Igayaza')
    village18 = Village.objects.create(parish=parish2, name='Kigoro')
    village19 = Village.objects.create(parish=parish2, name='Kigango')
    village20 = Village.objects.create(parish=parish2, name='Kanyamiyaga')
    village21 = Village.objects.create(parish=parish2, name='Rwenkuba')
    village22 = Village.objects.create(parish=parish2, name='Kyakataara')
    village23 = Village.objects.create(parish=parish2, name='Myongo')
    village24 = Village.objects.create(parish=parish2, name='Rwamuhiigi')
    village25 = Village.objects.create(parish=parish2, name='Rugarama')
    village26 = Village.objects.create(parish=parish2, name='Nyakwebundika iii')
    village27 = Village.objects.create(parish=parish2, name='Nyakasa')

    # Create Parish and Villages - Kabare
    parish3 = Parish.objects.create(subcounty=subcounty, name='Kabare')
    village28 = Village.objects.create(parish=parish3, name='Akengiri')
    village29 = Village.objects.create(parish=parish3, name='Kabaare')
    village30 = Village.objects.create(parish=parish3, name='Galilaya')
    village31 = Village.objects.create(parish=parish3, name='Kayonza')
    village32 = Village.objects.create(parish=parish3, name='Kanyeganyegye')
    village33 = Village.objects.create(parish=parish3, name='Karuhama')
    village34 = Village.objects.create(parish=parish3, name='Kabura')
    village35 = Village.objects.create(parish=parish3, name='Ruhumba')
    village36 = Village.objects.create(parish=parish3, name='Ruhumba t/c')
    village37 = Village.objects.create(parish=parish3, name='Nshozi')
    village38 = Village.objects.create(parish=parish3, name='Orukiri')
    village39 = Village.objects.create(parish=parish3, name='Rubindi')
    village40 = Village.objects.create(parish=parish3, name='Rubindi t/c a')
    village41 = Village.objects.create(parish=parish3, name='Rubindi t/c b')

    # Create Parish and Villages - Karwesanga(rugaaga)
    parish4 = Parish.objects.create(subcounty=subcounty, name='Karwesanga(rugaaga)')
    village42 = Village.objects.create(parish=parish4, name='Akarungu')
    village43 = Village.objects.create(parish=parish4, name='Bugarama')
    village44 = Village.objects.create(parish=parish4, name='Butaturwa')
    village45 = Village.objects.create(parish=parish4, name='Kanyamisisa')
    village46 = Village.objects.create(parish=parish4, name='Kaihiro')
    village47 = Village.objects.create(parish=parish4, name='Rwobusiisi')
    village48 = Village.objects.create(parish=parish4, name='Karitanyohoka')
    village49 = Village.objects.create(parish=parish4, name='Karwensanga')
    village50 = Village.objects.create(parish=parish4, name='Rwanyakahikye')
    village51 = Village.objects.create(parish=parish4, name='Rwebihangare')
    village52 = Village.objects.create(parish=parish4, name='Nakasero')
    village53 = Village.objects.create(parish=parish4, name='Mushunga')
    village54 = Village.objects.create(parish=parish4, name='Nyakatookye')
    village55 = Village.objects.create(parish=parish4, name='Nyakabungo')

    # Create Parish and Villages - Kariro
    parish5 = Parish.objects.create(subcounty=subcounty, name='Kariro')
    village56 = Village.objects.create(parish=parish5, name='Bitereko')
    village57 = Village.objects.create(parish=parish5, name='Burebero')
    village58 = Village.objects.create(parish=parish5, name='Ihondero')
    village59 = Village.objects.create(parish=parish5, name='Katete')
    village60 = Village.objects.create(parish=parish5, name='Rwembirizi')
    village61 = Village.objects.create(parish=parish5, name='Kariro')
    village62 = Village.objects.create(parish=parish5, name='Nyantungu')
    village63 = Village.objects.create(parish=parish5, name='Kyatoko')
    village64 = Village.objects.create(parish=parish5, name='Kyeibumba')
    village65 = Village.objects.create(parish=parish5, name='Nyakabungo')

    # Create Parish and Villages - Bisya
    parish6 = Parish.objects.create(subcounty=subcounty, name='Bisya')
    village66 = Village.objects.create(parish=parish6, name='Bisya')
    village67 = Village.objects.create(parish=parish6, name='Rweminago')
    village68 = Village.objects.create(parish=parish6, name='Rwemiyenje')
    village69 = Village.objects.create(parish=parish6, name='Kyekurira')
    village70 = Village.objects.create(parish=parish6, name='Rwabashegu')
    village71 = Village.objects.create(parish=parish6, name='Nyakwebundika i')
    village72 = Village.objects.create(parish=parish6, name='Nyakwebundika ii')
    village73 = Village.objects.create(parish=parish6, name='Rwakigando')
    village74 = Village.objects.create(parish=parish6, name='Nyakarama')
    village75 = Village.objects.create(parish=parish6, name='Rubaare')

if __name__ == '__main__':
    populate_database()
