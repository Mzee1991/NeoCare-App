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

    # Create Subcounty - Kakiika
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Kakiika')

    # Create Parish - Bunutsya ward
    parish1 = Parish.objects.create(subcounty=subcounty, name='Bunutsya ward')
    village1 = Village.objects.create(parish=parish1, name='Akashengye')
    village2 = Village.objects.create(parish=parish1, name='Bunutsya')
    village3 = Village.objects.create(parish=parish1, name='Kaitambwa')
    village4 = Village.objects.create(parish=parish1, name='Kyahi')
    village5 = Village.objects.create(parish=parish1, name='Kaburangire')
    village6 = Village.objects.create(parish=parish1, name='Kagorogoro')
    village7 = Village.objects.create(parish=parish1, name='Rukiri')

    # Create Parish - Kakiika ward
    parish2 = Parish.objects.create(subcounty=subcounty, name='Kakiika ward')
    village8 = Village.objects.create(parish=parish2, name='Butagatsi')
    village9 = Village.objects.create(parish=parish2, name='Rwobuyenje')
    village10 = Village.objects.create(parish=parish2, name='Kacence east')
    village11 = Village.objects.create(parish=parish2, name='Kacence west')
    village12 = Village.objects.create(parish=parish2, name='Makenke')
    village13 = Village.objects.create(parish=parish2, name='Nyakabungo')
    village14 = Village.objects.create(parish=parish2, name='Nyakiziba')

    # Create Parish - Kakoma
    parish3 = Parish.objects.create(subcounty=subcounty, name='Kakoma')
    village15 = Village.objects.create(parish=parish3, name='Kempungu')
    village16 = Village.objects.create(parish=parish3, name='Kakoma')
    village17 = Village.objects.create(parish=parish3, name='Kyarwabuganda')
    village18 = Village.objects.create(parish=parish3, name='Katebe')

    # Create Parish - Nyarubanga
    parish4 = Parish.objects.create(subcounty=subcounty, name='Nyarubanga')
    village19 = Village.objects.create(parish=parish4, name='Buremba i')
    village20 = Village.objects.create(parish=parish4, name='Buremba ii')
    village21 = Village.objects.create(parish=parish4, name='Kabingo')
    village22 = Village.objects.create(parish=parish4, name='Kenkombe')
    village23 = Village.objects.create(parish=parish4, name='Rwemigina central')
    village24 = Village.objects.create(parish=parish4, name='Nyarubanga')
    village25 = Village.objects.create(parish=parish4, name='Kafunjo')
    village26 = Village.objects.create(parish=parish4, name='Rwebihuro')
    village27 = Village.objects.create(parish=parish4, name='Mbarara stock farm')

if __name__ == '__main__':
    populate_database()
