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
    # Create District - Ibanda
    district, _ = District.objects.get_or_create(name='Ibanda')

    # Create County/Municipality - Ibanda south
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Ibanda south')

    # Create Subcounty - Kicuzi
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kicuzi')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Kicuzi', ['Brazil', 'Kabende', 'Kisabo', 'Kogabi', 'Kinyamugara', 'Kitehe', 'Kicuzi', 'Kategure', 'Katerera', 'Kagorogoro', 'Rwemambo', 'Kabuhwa', 'Mahuha', 'Murangara', 'Muture', 'Rugarama']),
        ('Kanywambogo', ['Kaabuhweju', 'Kisabo central', 'Kisabo i', 'Kisabo ii', 'Kibingo', 'Ryabatenga i', 'Ryabatenga ii', 'Ryakagumba']),
        ('Irimya', ['Buhindagi', 'Irimya', 'Kwerebera', 'Kitooma', 'Rwebiyongi', 'Kagyezi', 'Katongole', 'Kakindo', 'Ryakazo', 'Karokarungi', 'Karuhutsi', 'Rwenzigye', 'Mirama']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()