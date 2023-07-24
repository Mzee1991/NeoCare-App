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

    # Create Subcounty - Kakoba
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Kakoba')

    # Create Parish - Kakoba
    parish1 = Parish.objects.create(subcounty=subcounty, name='Kakoba')
    village1 = Village.objects.create(parish=parish1, name='Kihindi')
    village2 = Village.objects.create(parish=parish1, name='Kisenyi a')
    village3 = Village.objects.create(parish=parish1, name='Kishwahili')
    village4 = Village.objects.create(parish=parish1, name='Kakoba central')
    village5 = Village.objects.create(parish=parish1, name='Kakoba quarters')
    village6 = Village.objects.create(parish=parish1, name='Rwentondo')
    village7 = Village.objects.create(parish=parish1, name='Kyapotani')
    village8 = Village.objects.create(parish=parish1, name='N.t.c')
    village9 = Village.objects.create(parish=parish1, name='Mandela')
    village10 = Village.objects.create(parish=parish1, name='Lugazi')
    village11 = Village.objects.create(parish=parish1, name='Police/prisons')
    village12 = Village.objects.create(parish=parish1, name='Nyakaizi')

    # Create Parish - Nyamityobora
    parish2 = Parish.objects.create(subcounty=subcounty, name='Nyamityobora')
    village13 = Village.objects.create(parish=parish2, name='Agip')
    village14 = Village.objects.create(parish=parish2, name='Kabateraine')
    village15 = Village.objects.create(parish=parish2, name='Kilembe')
    village16 = Village.objects.create(parish=parish2, name='Central')
    village17 = Village.objects.create(parish=parish2, name='Lower')
    village18 = Village.objects.create(parish=parish2, name='Lubiri')
    village19 = Village.objects.create(parish=parish2, name='Market')
    village20 = Village.objects.create(parish=parish2, name='Muti')
    village21 = Village.objects.create(parish=parish2, name='Upper')
    village22 = Village.objects.create(parish=parish2, name='Survey')

if __name__ == '__main__':
    populate_database()
