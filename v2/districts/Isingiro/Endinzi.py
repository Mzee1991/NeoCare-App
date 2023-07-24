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
    district, _ = District.objects.get_or_create(name='Isingiro')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Bukanga')

    # Create Subcounty
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Endinzi')

    # Create Parish - Rwanjogyera
    parish1, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Rwanjogyera')

    # Create Villages for Rwanjogyera
    villages_rwanjogyera = [
        ('Rwenkuba a'), ('Rwenkuba b'), ('Karerabaana'), ('Rwakishayaya'),
        ('Rwanjogyera a'), ('Rwanjogyera b'), ('Rwanjogyera c'), ('Rwakasasira'),
        ('Rwakasasira b')
    ]
    for village_name in villages_rwanjogyera:
        village, _ = Village.objects.get_or_create(parish=parish1, name=village_name)

    # Create Parish - Rukungiri
    parish2, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Rukungiri')

    # Create Villages for Rukungiri
    villages_rukungiri = [
        ('Akatooma'), ('Rwakakore'), ('Rutunga'), ('Rukungiri')
    ]
    for village_name in villages_rukungiri:
        village, _ = Village.objects.get_or_create(parish=parish2, name=village_name)

    # Create Parish - Nyabyondo
    parish3, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Nyabyondo')

    # Create Villages for Nyabyondo
    villages_nyabyondo = [
        ('Ekiyonza'), ('Nyanja'), ('Kashoga'), ('Kamuzinzi'),
        ('Mpikye'), ('Nyabyondo'), ('Obunazi')
    ]
    for village_name in villages_nyabyondo:
        village, _ = Village.objects.get_or_create(parish=parish3, name=village_name)

    # Create Parish - Kikoba
    parish4, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Kikoba')

    # Create Villages for Kikoba
    villages_kikoba = [
        ('Kabarongo'), ('Kikoba a'), ('Kikoba b'), ('Ekitoka'),
        ('Kamaaya a'), ('Kamaaya b'), ('Kamaaya c'), ('Katanga a'), ('Katanga b')
    ]
    for village_name in villages_kikoba:
        village, _ = Village.objects.get_or_create(parish=parish4, name=village_name)

    # Create Parish - Busheka
    parish5, _ = Parish.objects.get_or_create(subcounty=subcounty, name='Busheka')

    # Create Villages for Busheka
    villages_busheka = [
        ('Busheka'), ('Ekinazi'), ('Kamwema a'), ('Kagaaga'),
        ('Rwambaga'), ('Mugugu'), ('Matara'), ('Ntuura')
    ]
    for village_name in villages_busheka:
        village, _ = Village.objects.get_or_create(parish=parish5, name=village_name)

if __name__ == '__main__':
    populate_database()
