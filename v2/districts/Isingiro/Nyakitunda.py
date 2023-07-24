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

def create_villages(parish, village_names):
    for village_name in village_names:
        Village.objects.get_or_create(parish=parish, name=village_name)

def populate_database():
    # Create District - Isingiro
    district, _ = District.objects.get_or_create(name='Isingiro')

    # Create County/Municipality - Isingiro north
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Isingiro north')

    # Create Subcounty/Town Council/Division - Nyakitunda
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Nyakitunda')

    # Create Parishes and Villages
    parishes = [
        ('Ruhira', ['Kabare', 'Kishenyi i', 'Kishenyi ii', 'Kahurwa i', 'Kahurwa ii', 'Kanyerere', 'Karundi i', 'Karundi ii', 'Rugongi i', 'Rugongi ii', 'Ruhiira ii', 'Ruhira i', 'Ngoma cell', 'Nyakamuri i', 'Nyakamuri ii', 'Omwicwamba', 'Town cell']),
        ('Migyera', ['Kagongi i', 'Kagongi ii', 'Migyera central', 'Migyera i', 'Migyera ii', 'Rwakibezi i', 'Rwakibezi ii']),
        ('Nyakarambi', ['Keitanyonyi', 'Nyangorogoro', 'Kabugu', 'Mburamaizi', 'Rugazi', 'Nyakabungo', 'Omubushami', 'Omukiniika i', 'Omukinika ii', 'Omunonko', 'Omurutooma', 'Nyakarambi i', 'Nyakarambi ii']),
        ('Ntungu', ['Birara', 'Ishingisha', 'Keina i', 'Keina ii', 'Kimbugu', 'Kitojo', 'Kyandaro', 'Kyanyakahimbi i', 'Kyanyakahimbi ii', 'Kasharira', 'Mahaama', 'Maju', 'Rugorogoro', 'Nyakahandagazi', 'Omukatooma', 'Omukitooma', 'Ntungu central', 'Ntungu trading centre', 'Ntungu west', 'Omurwerere']),
        ('Kihiihi', ['Kihiihi central', 'Kihiihi i', 'Kihiihi ii', 'Kihiihi town', 'Keina', 'Kyaaya', 'Kituro', 'Rwekishojwa i', 'Rwekishojwa ii', 'Rwembogo', 'Rwemondo', 'Nyandama', 'Nyanja-etagyera i', 'Nyanja-etagyera ii', 'Nyanja-etagyera iii', 'Mirambiro', 'Mbare', 'Nyakabungo']),
        ('Kamubeizi', ['Kabeshekyere', 'Kifumbira', 'Kibuba', 'Kagorora', 'Katojo', 'Nyamiyaga', 'Katukundane', 'Karo - karungi', 'Kashaki', 'Kashenyi', 'Kyarugoonza', 'Kagarama', 'Kanani', 'Nyamirama', 'Rwacece', 'Nyakabungo', 'Rushoroza']),
        ('Bugongi', ['Bugongi i', 'Bugongi ii', 'Kamiranjogyera i', 'Kamiranjogyera ii', 'Kyefurwe', 'Rwanyinamagangure i', 'Rwanyinamagangure ii', 'Omukabale', 'Omukanara', 'Omukihangire', 'Omukihimba', 'Omukinazi', 'Town cell', 'Nyaruhanga', 'Nyarushanje'])
    ]

    for parish_name, village_names in parishes:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        create_villages(parish, village_names)

if __name__ == '__main__':
    populate_database()