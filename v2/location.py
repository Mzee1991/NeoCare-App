#!/usr/bin/python3

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from newborn.models import District, Subcounty, Parish, Village

def populate_database():
    # Create Districts
    district1 = District.objects.create(name='Kampala')
    district2 = District.objects.create(name='Jinja')

    # Create Subcounties
    subcounty1 = Subcounty.objects.create(district=district1, name='Makindye')
    subcounty2 = Subcounty.objects.create(district=district1, name='Nakawa')
    subcounty3 = Subcounty.objects.create(district=district2, name='Jinja East')
    subcounty4 = Subcounty.objects.create(district=district2, name='Jinja West')

    # Create Parishes
    parish1 = Parish.objects.create(subcounty=subcounty1, name='Kibuye')
    parish2 = Parish.objects.create(subcounty=subcounty1, name='Lukuli')
    parish3 = Parish.objects.create(subcounty=subcounty2, name='Ntinda')
    parish4 = Parish.objects.create(subcounty=subcounty2, name='Nakawa')
    parish5 = Parish.objects.create(subcounty=subcounty3, name='Mpumudde')
    parish6 = Parish.objects.create(subcounty=subcounty3, name='Bugembe')
    parish7 = Parish.objects.create(subcounty=subcounty4, name='Majengo')
    parish8 = Parish.objects.create(subcounty=subcounty4, name='Wairaka')

    # Create Villages
    village1 = Village.objects.create(parish=parish1, name='Kibuye Village 1')
    village2 = Village.objects.create(parish=parish1, name='Kibuye Village 2')
    village3 = Village.objects.create(parish=parish2, name='Lukuli Village 1')
    village4 = Village.objects.create(parish=parish2, name='Lukuli Village 2')
    village5 = Village.objects.create(parish=parish3, name='Ntinda Village 1')
    village6 = Village.objects.create(parish=parish3, name='Ntinda Village 2')
    village7 = Village.objects.create(parish=parish4, name='Nakawa Village 1')
    village8 = Village.objects.create(parish=parish4, name='Nakawa Village 2')
    village9 = Village.objects.create(parish=parish5, name='Mpumudde Village 1')
    village10 = Village.objects.create(parish=parish5, name='Mpumudde Village 2')
    village11 = Village.objects.create(parish=parish6, name='Bugembe Village 1')
    village12 = Village.objects.create(parish=parish6, name='Bugembe Village 2')
    village13 = Village.objects.create(parish=parish7, name='Majengo Village 1')
    village14 = Village.objects.create(parish=parish7, name='Majengo Village 2')
    village15 = Village.objects.create(parish=parish8, name='Wairaka Village 1')
    village16 = Village.objects.create(parish=parish8, name='Wairaka Village 2')

if __name__ == '__main__':
    populate_database()
