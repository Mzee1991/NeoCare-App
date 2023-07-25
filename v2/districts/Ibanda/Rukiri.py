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

    # Create Subcounty - Rukiri
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Rukiri')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Nyarukiika', ['Kaiho', 'Rwensiga i', 'Rwensiga ii', 'Kyeitana', 'Kyezitira i', 'Kyezitira ii', 'Rugarama i', 'Rugarama ii', 'Nyakayojo', 'Rutooma', 'Nyarwato']),
        ('Mpasha', ['Kaarangara', 'Rwengorogoro', 'Ryakashunsha', 'Karombe', 'Kyanika', 'Mpasha', 'Muhangi']),
        ('Kigunga', ['Kabingo', 'Kisensero', 'Rwobuhungye', 'Njembe i', 'Njembe ii', 'Nyakahita']),
        ('Mabona', ['Kaara', 'Kabingo', 'Kitengure', 'Karihe', 'Ryamitamba', 'Mabona', 'Rugazi', 'Vatican']),
        ('Katembe', ['Ihome', 'Bwahika', 'Kibande i', 'Kibande ii', 'Katembe', 'Kaijororonga', 'Ryakatiri', 'Rwijogoro', 'Kashari', 'Mugarama i', 'Mugarama ii', 'Nyarubira']),
        ('Bwenda', ['Bwenda', 'Rwobuhompo', 'Mirambi i', 'Mirambi ii', 'Mpunda', 'Rukiiri', 'Ntanga']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()