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
    # District: Isingiro
    district, _ = District.objects.get_or_create(name='Isingiro')

    # County/Municipality: Isingiro north
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Isingiro north')

    # Sub-County/Town Council/Division: Isingiro town council
    subcounty1, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Isingiro town council')

    # Parish: Rwetango
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Rwetango')

    # Villages for Rwetango
    villages_rwetango = ['Bushenga', 'Humura', 'Igayaza', 'Kabingo central', 'Kabingo ii', 'Kaharo', 'Ryamihini', 'Kyamusyoka', 'Masha', 'Nyakisharara']
    for village_name in villages_rwetango:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Parish: Rwekubo
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Rwekubo')

    # Villages for Rwekubo
    villages_rwekubo = ['Ishoozi', 'Kayonza', 'Kayonza central', 'Rwekubo', 'Kahirimbi', 'Kajurungutsi', 'Katwengye', 'Rwenkuba', 'Kakunyu', 'Kyakashana', 'Misirira']
    for village_name in villages_rwekubo:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Parish: Mabona
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Mabona')

    # Villages for Mabona
    villages_mabona = ['Kibingo', 'Kigarama', 'Kibwera central', 'Kyabirukwa', 'Kyamudima', 'Kyeihenda', 'Mabona', 'Mahwa', 'Makiro', 'Mbaare', 'Nyakabanga']
    for village_name in villages_mabona:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Parish: Kyabishaho ward
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Kyabishaho ward')

    # Villages for Kyabishaho ward
    villages_kyabishaho = ['Akataffaari', 'Kikoona', 'Kigando', 'Kanyerere', 'Kyabishaho', 'Kakinga', 'Kacunuzi', 'Rubweijana']
    for village_name in villages_kyabishaho:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

    # Parish: Kamuri ward
    parish5, _ = Parish.objects.get_or_create(subcounty=subcounty1, name='Kamuri ward')

    # Villages for Kamuri ward
    villages_kamuri = ['Buheigoore', 'Kabare', 'Kigyende', 'Kikutsi', 'Rwembwa', 'Rwendama', 'Rwengiri', 'Rwentongore', 'Kyarwamutambara', 'Ruhimbo']
    for village_name in villages_kamuri:
        village, _ = Village.objects.get_or_create(parish=parish5, name=village_name)

if __name__ == '__main__':
    populate_database()