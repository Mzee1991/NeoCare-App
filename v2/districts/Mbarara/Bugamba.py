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
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Bugamba')

    # Create Parish - Kabarama
    parish1 = Parish.objects.create(subcounty=subcounty, name='Kabarama')
    village1 = Village.objects.create(parish=parish1, name='Kabarama i')
    village2 = Village.objects.create(parish=parish1, name='Kabarama ii')
    village3 = Village.objects.create(parish=parish1, name='Byanamira')
    village4 = Village.objects.create(parish=parish1, name='Kayunga')
    village5 = Village.objects.create(parish=parish1, name='Kanyangongi')
    village6 = Village.objects.create(parish=parish1, name='Katinda')
    village7 = Village.objects.create(parish=parish1, name='Kakyerere')
    village8 = Village.objects.create(parish=parish1, name='Nyarubare i')
    village9 = Village.objects.create(parish=parish1, name='Nyarubare ii')
    village10 = Village.objects.create(parish=parish1, name='Kamishate')
    village11 = Village.objects.create(parish=parish1, name='Mparamo')
    village12 = Village.objects.create(parish=parish1, name='Rurama')
    village13 = Village.objects.create(parish=parish1, name='Rurengye')
    village14 = Village.objects.create(parish=parish1, name='Nyakasana')
    village15 = Village.objects.create(parish=parish1, name='Rubingo i')
    village16 = Village.objects.create(parish=parish1, name='Rubingo ii')

    # Create Parish - Kamomo
    parish2 = Parish.objects.create(subcounty=subcounty, name='Kamomo')
    village17 = Village.objects.create(parish=parish2, name='Bushaaka')
    village18 = Village.objects.create(parish=parish2, name='Buranga')
    village19 = Village.objects.create(parish=parish2, name='Rwenkwanzi')
    village20 = Village.objects.create(parish=parish2, name='Kabukara')
    village21 = Village.objects.create(parish=parish2, name='Kashenyi')
    village22 = Village.objects.create(parish=parish2, name='Rwamuhurira')
    village23 = Village.objects.create(parish=parish2, name='Nshuro')
    village24 = Village.objects.create(parish=parish2, name='Nyarwina')

    # Create Parish - Kibingo
    parish3 = Parish.objects.create(subcounty=subcounty, name='Kibingo')
    village25 = Village.objects.create(parish=parish3, name='Buterere')
    village26 = Village.objects.create(parish=parish3, name='Kikukuru')
    village27 = Village.objects.create(parish=parish3, name='Kibingo')
    village28 = Village.objects.create(parish=parish3, name='Ekihena')
    village29 = Village.objects.create(parish=parish3, name='Rwamuganga')
    village30 = Village.objects.create(parish=parish3, name='Kyetindo')
    village31 = Village.objects.create(parish=parish3, name='Rushanje')
    village32 = Village.objects.create(parish=parish3, name='Nyakabungo')
    village33 = Village.objects.create(parish=parish3, name='Ntsingwa i')
    village34 = Village.objects.create(parish=parish3, name='Ntsingwa ii')

    # Create Parish - Ngugo
    parish4 = Parish.objects.create(subcounty=subcounty, name='Ngugo')
    village35 = Village.objects.create(parish=parish4, name='Binyuga')
    village36 = Village.objects.create(parish=parish4, name='Bituntu')
    village37 = Village.objects.create(parish=parish4, name='Kaaya')
    village38 = Village.objects.create(parish=parish4, name='Kikuto i')
    village39 = Village.objects.create(parish=parish4, name='Kikuto ii')
    village40 = Village.objects.create(parish=parish4, name='Kigando')
    village41 = Village.objects.create(parish=parish4, name='Kakongora i')
    village42 = Village.objects.create(parish=parish4, name='Kakongora ii')
    village43 = Village.objects.create(parish=parish4, name='Ngugo i')
    village44 = Village.objects.create(parish=parish4, name='Ngugo ii')

    # Create Parish - Nyaruhandagazi
    parish5 = Parish.objects.create(subcounty=subcounty, name='Nyaruhandagazi')
    village45 = Village.objects.create(parish=parish5, name='Bushoro')
    village46 = Village.objects.create(parish=parish5, name='Kigando')
    village47 = Village.objects.create(parish=parish5, name='Kitooha')
    village48 = Village.objects.create(parish=parish5, name='Kashekure')
    village49 = Village.objects.create(parish=parish5, name='Kashungwe')
    village50 = Village.objects.create(parish=parish5, name='Misibika')
    village51 = Village.objects.create(parish=parish5, name='Rugorogoro')
    village52 = Village.objects.create(parish=parish5, name='Nyamabare')
    village53 = Village.objects.create(parish=parish5, name='Nyakibare')
    village54 = Village.objects.create(parish=parish5, name='Ntungamo')
    village55 = Village.objects.create(parish=parish5, name='Nyaruhandagazi i')
    village56 = Village.objects.create(parish=parish5, name='Nyaruhandagazi ii')
    village57 = Village.objects.create(parish=parish5, name='Nyarwambu')

    # Create Parish - Rweibogo
    parish6 = Parish.objects.create(subcounty=subcounty, name='Rweibogo')
    village58 = Village.objects.create(parish=parish6, name='Bugamba')
    village59 = Village.objects.create(parish=parish6, name='Byanamira')
    village60 = Village.objects.create(parish=parish6, name='Katerero')
    village61 = Village.objects.create(parish=parish6, name='Rweibogo i')
    village62 = Village.objects.create(parish=parish6, name='Rweibogo ii')
    village63 = Village.objects.create(parish=parish6, name='Rwemisha')
    village64 = Village.objects.create(parish=parish6, name='Mweya')
    village65 = Village.objects.create(parish=parish6, name='Ruzinga')

if __name__ == '__main__':
    populate_database()
