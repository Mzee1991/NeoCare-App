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
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Mbarara Municipality')

    # Create Subcounty
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Nyamitanga')

    # Create Parish - Ruti
    parish1 = Parish.objects.create(subcounty=subcounty, name='Ruti')

    # Create Villages for Ruti
    village1 = Village.objects.create(parish=parish1, name='Kirehe')
    village2 = Village.objects.create(parish=parish1, name='Nyamitanga')
    village3 = Village.objects.create(parish=parish1, name='Rwizi')
    village4 = Village.objects.create(parish=parish1, name='Kafunda')
    village5 = Village.objects.create(parish=parish1, name='Kateera')
    village6 = Village.objects.create(parish=parish1, name='Market')
    village7 = Village.objects.create(parish=parish1, name='Nsikye')
    village8 = Village.objects.create(parish=parish1, name='Tankhill')

    # Create Parish - Katete
    parish2 = Parish.objects.create(subcounty=subcounty, name='Katete')

    # Create Villages for Katete
    village9 = Village.objects.create(parish=parish2, name='Bihunya')
    village10 = Village.objects.create(parish=parish2, name='Kitebero')
    village11 = Village.objects.create(parish=parish2, name='Katete central')
    village12 = Village.objects.create(parish=parish2, name='Nyamitanga')
    village13 = Village.objects.create(parish=parish2, name='Rwemirinzi')
    village14 = Village.objects.create(parish=parish2, name='Karugangama')
    village15 = Village.objects.create(parish=parish2, name='Rwizi')
    village16 = Village.objects.create(parish=parish2, name='Nsikye')

if __name__ == '__main__':
    populate_database()
