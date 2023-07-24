#!/usr/bin/python3
import sys
import os
import django

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
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Bubaare')

    # Create Parish and Villages - Rwenshanku
    parish1 = Parish.objects.create(subcounty=subcounty, name='Rwenshanku')
    village1 = Village.objects.create(parish=parish1, name='Bubaare i')
    village2 = Village.objects.create(parish=parish1, name='Bubaare ii')
    village3 = Village.objects.create(parish=parish1, name='Rwenturagara')
    village4 = Village.objects.create(parish=parish1, name='Rwenshanku')
    village5 = Village.objects.create(parish=parish1, name='Rugongi')

    # Create Parish and Villages - Rugarama
    parish2 = Parish.objects.create(subcounty=subcounty, name='Rugarama')
    village6 = Village.objects.create(parish=parish2, name='Kitojo')
    village7 = Village.objects.create(parish=parish2, name='Rugarama i')
    village8 = Village.objects.create(parish=parish2, name='Rugarama ii')
    village9 = Village.objects.create(parish=parish2, name='Nkaaka')

    # Create Parish and Villages - Katojo
    parish3 = Parish.objects.create(subcounty=subcounty, name='Katojo')
    village10 = Village.objects.create(parish=parish3, name='Kifunfu')
    village11 = Village.objects.create(parish=parish3, name='Katojo i')
    village12 = Village.objects.create(parish=parish3, name='Katojo ii')
    village13 = Village.objects.create(parish=parish3, name='Kafunjo')
    village14 = Village.objects.create(parish=parish3, name='Rubingo')

    # Create Parish and Villages - Kashaka
    parish4 = Parish.objects.create(subcounty=subcounty, name='Kashaka')
    village15 = Village.objects.create(parish=parish4, name='Nyamitooma')
    village16 = Village.objects.create(parish=parish4, name='Rwengyenyi')
    village17 = Village.objects.create(parish=parish4, name='Rwentondo')
    village18 = Village.objects.create(parish=parish4, name='Kashaka i/kobwoba')
    village19 = Village.objects.create(parish=parish4, name='Rwanyampazi')
    village20 = Village.objects.create(parish=parish4, name='Nyabugando')
    village21 = Village.objects.create(parish=parish4, name='Nshozi/kaisyoro')
    village22 = Village.objects.create(parish=parish4, name='Rushasha')

    # Create Parish and Villages - Kamushoko
    parish5 = Parish.objects.create(subcounty=subcounty, name='Kamushoko')
    village23 = Village.objects.create(parish=parish5, name='Kaiba')
    village24 = Village.objects.create(parish=parish5, name='Rwempogo')
    village25 = Village.objects.create(parish=parish5, name='Rwobuyenje')
    village26 = Village.objects.create(parish=parish5, name='Kakumba')
    village27 = Village.objects.create(parish=parish5, name='Kyantamba')
    village28 = Village.objects.create(parish=parish5, name='Rwambabana')

    # Create Parish and Villages - Mugarusya
    parish6 = Parish.objects.create(subcounty=subcounty, name='Mugarusya')
    village29 = Village.objects.create(parish=parish6, name='Kanyara i')
    village30 = Village.objects.create(parish=parish6, name='Kanyara ii')
    village31 = Village.objects.create(parish=parish6, name='Mugarutsya i')
    village32 = Village.objects.create(parish=parish6, name='Mugarutsya ii')
    village33 = Village.objects.create(parish=parish6, name='Mugarutsya iii')
    village34 = Village.objects.create(parish=parish6, name='Mutumo')

if __name__ == '__main__':
    populate_database()
