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
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Rubaya - Mbarara')

    # Create Parish and Villages - Rushozi
    parish1 = Parish.objects.create(subcounty=subcounty, name='Rushozi')
    village1 = Village.objects.create(parish=parish1, name='Rwenkanja')
    village2 = Village.objects.create(parish=parish1, name='Kakono')
    village3 = Village.objects.create(parish=parish1, name='Nyantungu')
    village4 = Village.objects.create(parish=parish1, name='Kyamatambarire i')
    village5 = Village.objects.create(parish=parish1, name='Kyamatambarire ii')
    village6 = Village.objects.create(parish=parish1, name='Kanga')
    village7 = Village.objects.create(parish=parish1, name='Muko')
    village8 = Village.objects.create(parish=parish1, name='Rwabaranga')

    # Create Parish and Villages - Ruhunga
    parish2 = Parish.objects.create(subcounty=subcounty, name='Ruhunga')
    village9 = Village.objects.create(parish=parish2, name='Keigoshora')
    village10 = Village.objects.create(parish=parish2, name='Ekiyayo')
    village11 = Village.objects.create(parish=parish2, name='Geitemba')
    village12 = Village.objects.create(parish=parish2, name='Katete')
    village13 = Village.objects.create(parish=parish2, name='Kaguhanzya')
    village14 = Village.objects.create(parish=parish2, name='Kaiho')
    village15 = Village.objects.create(parish=parish2, name='Kashenyi')
    village16 = Village.objects.create(parish=parish2, name='Rugyerera')
    village17 = Village.objects.create(parish=parish2, name='Ruhunga central')
    village18 = Village.objects.create(parish=parish2, name='Ruhunga i')
    village19 = Village.objects.create(parish=parish2, name='Ruhunga ii')
    village20 = Village.objects.create(parish=parish2, name='Nyakibungo')

    # Create Parish and Villages - Ruburara
    parish3 = Parish.objects.create(subcounty=subcounty, name='Ruburara')
    village21 = Village.objects.create(parish=parish3, name='Ekigando')
    village22 = Village.objects.create(parish=parish3, name='Kahoma')
    village23 = Village.objects.create(parish=parish3, name='Kaburamuriro')
    village24 = Village.objects.create(parish=parish3, name='Mutonto')
    village25 = Village.objects.create(parish=parish3, name='Ruburara i')
    village26 = Village.objects.create(parish=parish3, name='Ruburara ii')

    # Create Parish and Villages - Bunenero
    parish4 = Parish.objects.create(subcounty=subcounty, name='Bunenero')
    village27 = Village.objects.create(parish=parish4, name='Bunenero')
    village28 = Village.objects.create(parish=parish4, name='Ekitete')
    village29 = Village.objects.create(parish=parish4, name='Kabwera')
    village30 = Village.objects.create(parish=parish4, name='Rwatsinga')
    village31 = Village.objects.create(parish=parish4, name='Rugarama')
    village32 = Village.objects.create(parish=parish4, name='Ruyonza')
    village33 = Village.objects.create(parish=parish4, name='Rukukuru')
    village34 = Village.objects.create(parish=parish4, name='Rubaya')

    # Create Parish and Villages - Itara
    parish5 = Parish.objects.create(subcounty=subcounty, name='Itara')
    village35 = Village.objects.create(parish=parish5, name='Ekirehe i')
    village36 = Village.objects.create(parish=parish5, name='Ekirehe ii')
    village37 = Village.objects.create(parish=parish5, name='Ekyeera i')
    village38 = Village.objects.create(parish=parish5, name='Ekyeera ii')
    village39 = Village.objects.create(parish=parish5, name='Ekyeera iii')
    village40 = Village.objects.create(parish=parish5, name='Kyarwamaganda')
    village41 = Village.objects.create(parish=parish5, name='Rukukuru')

if __name__ == '__main__':
    populate_database()
