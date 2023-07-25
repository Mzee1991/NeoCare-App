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

    # Create County/Municipality - Ibanda north
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Ibanda north')

    # Create Subcounty - Ishongororo
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Ishongororo')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Muziza', ['Akabare', 'Karambi', 'Kakuuto i', 'Kakuuto ii', 'Kakuuto iii', 'Kashagazi', 'Kyembogo', 'Kyembogo ii', 'Mwana', 'Mwana ii', 'Mugondo']),
        ('Mushunga', ['Kitooro i', 'Kitooro ii', 'Rwebirago', 'Rwetweka i', 'Rwetweka ii', 'Mushunga i', 'Mushunga ii', 'Mushunga iii', 'Rugando i', 'Rugando ii']),
        ('Kashozi', ['Katehe', 'Katengyeto', 'Katojo i', 'Katojo ii', 'Katwe i', 'Katwe ii', 'Kakiro', 'Kyanyamarembo', 'Kashozi', 'Kaniampiha', 'Rushambya']),
        ('Birongo', ['Birongo ii', 'Birongo iii', 'Birongo iv', 'Kaarokarungi', 'Kabiso', 'Kahoko', 'Kafunjo i', 'Kafunjo ii', 'Kafunjo iii', 'Mutengyeto', 'Nyamabaare', 'Ntusi i', 'Ntusi ii']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()