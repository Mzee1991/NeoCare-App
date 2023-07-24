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

    # Create Subcounty - Kamukuzi
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Kamukuzi')

    # Create Parish - Kamukuzi
    parish1 = Parish.objects.create(subcounty=subcounty, name='Kamukuzi')
    village1 = Village.objects.create(parish=parish1, name='Baifra')
    village2 = Village.objects.create(parish=parish1, name='Booma')
    village3 = Village.objects.create(parish=parish1, name='Rwebikoona')
    village4 = Village.objects.create(parish=parish1, name='Kakiika')
    village5 = Village.objects.create(parish=parish1, name='Kakyeka')
    village6 = Village.objects.create(parish=parish1, name='Kashanyarazi')
    village7 = Village.objects.create(parish=parish1, name='Kamukuzi')
    village8 = Village.objects.create(parish=parish1, name='Medical')
    village9 = Village.objects.create(parish=parish1, name='Ntare')

    # Create Parish - Ruharo
    parish2 = Parish.objects.create(subcounty=subcounty, name='Ruharo')
    village10 = Village.objects.create(parish=parish2, name='Kiyanja')
    village11 = Village.objects.create(parish=parish2, name='Rwizi')
    village12 = Village.objects.create(parish=parish2, name='Mbaguta')
    village13 = Village.objects.create(parish=parish2, name='Mbarara high school')
    village14 = Village.objects.create(parish=parish2, name='Nkokonjeru')

if __name__ == '__main__':
    populate_database()
