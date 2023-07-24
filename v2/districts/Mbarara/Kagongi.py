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
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Kagongi')

    # Create Parish and Villages - Ntuura
    parish1 = Parish.objects.create(subcounty=subcounty, name='Ntuura')
    village1 = Village.objects.create(parish=parish1, name='Akakinga')
    village2 = Village.objects.create(parish=parish1, name='Akacuucu')
    village3 = Village.objects.create(parish=parish1, name='Keishenuma')
    village4 = Village.objects.create(parish=parish1, name='Rweera')
    village5 = Village.objects.create(parish=parish1, name='Kyarushanje')
    village6 = Village.objects.create(parish=parish1, name='Mitooma')
    village7 = Village.objects.create(parish=parish1, name='Nyaminyobwa')
    village8 = Village.objects.create(parish=parish1, name='Nkondo')
    village9 = Village.objects.create(parish=parish1, name='Nsiika')
    village10 = Village.objects.create(parish=parish1, name='Omukagyera')
    village11 = Village.objects.create(parish=parish1, name='Ntuura')

    # Create Parish and Villages - Nsiika
    parish2 = Parish.objects.create(subcounty=subcounty, name='Nsiika')
    village12 = Village.objects.create(parish=parish2, name='Akakinga')
    village13 = Village.objects.create(parish=parish2, name='Akanago')
    village14 = Village.objects.create(parish=parish2, name='Kibega')
    village15 = Village.objects.create(parish=parish2, name='Ekicundezi')
    village16 = Village.objects.create(parish=parish2, name='Ekimoma')
    village17 = Village.objects.create(parish=parish2, name='Kahiihi')
    village18 = Village.objects.create(parish=parish2, name='Kanyinansiika')
    village19 = Village.objects.create(parish=parish2, name='Nsiika')

    # Create Parish and Villages - Ngango
    parish3 = Parish.objects.create(subcounty=subcounty, name='Ngango')
    village20 = Village.objects.create(parish=parish3, name='Akashenshero')
    village21 = Village.objects.create(parish=parish3, name='Akagyera i')
    village22 = Village.objects.create(parish=parish3, name='Akagyera ii')
    village23 = Village.objects.create(parish=parish3, name='Ekikaira')
    village24 = Village.objects.create(parish=parish3, name='Rwemirama')
    village25 = Village.objects.create(parish=parish3, name='Ryakajumba')
    village26 = Village.objects.create(parish=parish3, name='Kyakajebere')
    village27 = Village.objects.create(parish=parish3, name='Rweshe')
    village28 = Village.objects.create(parish=parish3, name='Kagongi')
    village29 = Village.objects.create(parish=parish3, name='Ngango')
    village30 = Village.objects.create(parish=parish3, name='Orurembo')

    # Create Parish and Villages - Kyandahi
    parish4 = Parish.objects.create(subcounty=subcounty, name='Kyandahi')
    village31 = Village.objects.create(parish=parish4, name='Akakatsi')
    village32 = Village.objects.create(parish=parish4, name='Akatongore')
    village33 = Village.objects.create(parish=parish4, name='Bugarama')
    village34 = Village.objects.create(parish=parish4, name='Kabare')
    village35 = Village.objects.create(parish=parish4, name='Kyabamuhiga')
    village36 = Village.objects.create(parish=parish4, name='Kyarugabirana')
    village37 = Village.objects.create(parish=parish4, name='Nyabuhaama')
    village38 = Village.objects.create(parish=parish4, name='Nyakabwera')
    village39 = Village.objects.create(parish=parish4, name='Orurembo')

    # Create Parish and Villages - Kibingo
    parish5 = Parish.objects.create(subcounty=subcounty, name='Kibingo')
    village40 = Village.objects.create(parish=parish5, name='Akatooma')
    village41 = Village.objects.create(parish=parish5, name='Buzooba')
    village42 = Village.objects.create(parish=parish5, name='Keijororonga')
    village43 = Village.objects.create(parish=parish5, name='Kempiri')
    village44 = Village.objects.create(parish=parish5, name='Kibingo central')
    village45 = Village.objects.create(parish=parish5, name='Rwobuzani')
    village46 = Village.objects.create(parish=parish5, name='Kariire')
    village47 = Village.objects.create(parish=parish5, name='Rwiziringiro')
    village48 = Village.objects.create(parish=parish5, name='Kyandahi')
    village49 = Village.objects.create(parish=parish5, name='Kamuganga')
    village50 = Village.objects.create(parish=parish5, name='Mubanda')
    village51 = Village.objects.create(parish=parish5, name='Rwabashaki')

    # Create Parish and Villages - Bwengure
    parish6 = Parish.objects.create(subcounty=subcounty, name='Bwengure')
    village52 = Village.objects.create(parish=parish6, name='Bwengure')
    village53 = Village.objects.create(parish=parish6, name='Kibaare')
    village54 = Village.objects.create(parish=parish6, name='Nyamunyobwa')
    village55 = Village.objects.create(parish=parish6, name='Kyanyakwezi')
    village56 = Village.objects.create(parish=parish6, name='Kyarutahairwa')
    village57 = Village.objects.create(parish=parish6, name='Katagyengyera')
    village58 = Village.objects.create(parish=parish6, name='Mugugu')
    village59 = Village.objects.create(parish=parish6, name='Rugarama')
    village60 = Village.objects.create(parish=parish6, name='Nyakatookye')
    village61 = Village.objects.create(parish=parish6, name='Nyakabirizi')
    village62 = Village.objects.create(parish=parish6, name='Rubingo')

if __name__ == '__main__':
    populate_database()
