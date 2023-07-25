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

    # Create County/Municipality - Ibanda municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Ibanda municipality')

    # Create Subcounty - Bisheshe division
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Bisheshe division')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Rugazi ward', ['Bigyera', 'Kashaka i', 'Kashaka ii', 'Kyeikucu i', 'Kyeikucu ii', 'Rugazi i', 'Rugazi ii', 'Nyakatokye i', 'Nyakatokye ii']),
        ('Kigarama ward', ['Bukuuto', 'Kigarama lower', 'Kigarama t/c', 'Kigarama upper', 'Kagorogoro', 'Rwamabaare lower', 'Rwamabaare upper', 'Nyakatete i', 'Nyakatete ii', 'Nyakatete iii']),
        ('Kakatsi', ['Bishayumbe', 'Kakatsi i', 'Kakatsi ii', 'Kakatsi iii', 'Mishozi i', 'Mishozi ii', 'Mishozi iii']),
        ('Kabaare', ['Kabaare i', 'Kabaare ii', 'Kabaare iii', 'Keihiro i', 'Keihiro ii', 'Gabaruri', 'Kyembogo i', 'Kyembogo ii', 'Kagango i', 'Kagango ii', 'Kagango iii', 'Kagango iv', 'Kagango v', 'Rushaka i', 'Rushaka ii']),
        ('Rugazi ward', ['Bigyera', 'Kashaka i', 'Kashaka ii', 'Kyeikucu i', 'Kyeikucu ii', 'Rugazi i', 'Rugazi ii', 'Nyakatokye i', 'Nyakatokye ii']),
        ('Rugazi ward', ['Bigyera', 'Kashaka i', 'Kashaka ii', 'Kyeikucu i', 'Kyeikucu ii', 'Rugazi i', 'Rugazi ii', 'Nyakatokye i', 'Nyakatokye ii']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()