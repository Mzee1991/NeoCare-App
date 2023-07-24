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
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Bukiiro')

    # Create Parish and Villages - Nyarubungo
    parish1 = Parish.objects.create(subcounty=subcounty, name='Nyarubungo')
    village1 = Village.objects.create(parish=parish1, name='Akashanda')
    village2 = Village.objects.create(parish=parish1, name='Kibaare')
    village3 = Village.objects.create(parish=parish1, name='Kibaare b')
    village4 = Village.objects.create(parish=parish1, name='Kanyigiri')
    village5 = Village.objects.create(parish=parish1, name='Nyamunywanisa')
    village6 = Village.objects.create(parish=parish1, name='Rwentojo')
    village7 = Village.objects.create(parish=parish1, name='Rushenyi')
    village8 = Village.objects.create(parish=parish1, name='Orugando')
    village9 = Village.objects.create(parish=parish1, name='Nyarubungo')

    # Create Parish and Villages - Nyanja
    parish2 = Parish.objects.create(subcounty=subcounty, name='Nyanja')
    village10 = Village.objects.create(parish=parish2, name='Ihanika')
    village11 = Village.objects.create(parish=parish2, name='Kibazi')
    village12 = Village.objects.create(parish=parish2, name='Nyamirima a')
    village13 = Village.objects.create(parish=parish2, name='Nyamirima b')
    village14 = Village.objects.create(parish=parish2, name='Rwengwe')
    village15 = Village.objects.create(parish=parish2, name='Kyabiranga')
    village16 = Village.objects.create(parish=parish2, name='Nyanja a')
    village17 = Village.objects.create(parish=parish2, name='Nyanja b')

    # Create Parish and Villages - Rubingo
    parish3 = Parish.objects.create(subcounty=subcounty, name='Rubingo')
    village18 = Village.objects.create(parish=parish3, name='Kigoro')
    village19 = Village.objects.create(parish=parish3, name='Kagyera')
    village20 = Village.objects.create(parish=parish3, name='Rwentondo')
    village21 = Village.objects.create(parish=parish3, name='Nyantungu')
    village22 = Village.objects.create(parish=parish3, name='Rwamagaju')
    village23 = Village.objects.create(parish=parish3, name='Rubingo')
    village24 = Village.objects.create(parish=parish3, name='Rubingo central')

    # Create Parish and Villages - Bukiro
    parish4 = Parish.objects.create(subcounty=subcounty, name='Bukiro')
    village25 = Village.objects.create(parish=parish4, name='Bukiro')
    village26 = Village.objects.create(parish=parish4, name='Kaziga i')
    village27 = Village.objects.create(parish=parish4, name='Kaziga ii')
    village28 = Village.objects.create(parish=parish4, name='Kakondo i')
    village29 = Village.objects.create(parish=parish4, name='Kakondo ii')
    village30 = Village.objects.create(parish=parish4, name='Mirambi')
    village31 = Village.objects.create(parish=parish4, name='Rwamuganga')

if __name__ == '__main__':
    populate_database()
