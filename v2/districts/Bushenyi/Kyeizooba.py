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
    # Create District - Bushenyi
    district, _ = District.objects.get_or_create(name='Bushenyi')

    # Create County/Municipality - Igara east
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Igara east')

    # Create Subcounty - Kyeizooba
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kyeizooba')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Nyamiyaga', ['Bushenyi utc', 'Kabakobokye', 'Nyamiyaga', 'Nyampikye', 'Kyeizooba', 'Kangoma', 'Nyakashozi', 'Nyakinengo', 'Runyinya i', 'Runyinya ii']),
        ('Rutooma', ['Kihunda', 'Nyamirima', 'Katooma', 'Rwenkuba', 'Kyamagambo', 'Kandekye', 'Kantojo', 'Misingano', 'Rwanyankara', 'Mukama', 'Mbatamo', 'Nyabutobo', 'Rugunga', 'Omukibare', 'Nyarurambi']),
        ('Ntungamo', ['Rwamukooto', 'Rwakahuka', 'Nshenga', 'Ntungamo']),
        ('Kitwe', ['Kyabasenene', 'Kitwe', 'Rwentuha', 'Kashogashoga', 'Kancucu', 'Ncucumo', 'Rwagasha', 'Rutooma', 'Rushoga', 'Omukacence', 'Omunjeru', 'Rubingo']),
        ('Kitagata', ['Itega', 'Kibaniga i', 'Kibaniga ii', 'Kitagata', 'Kanyamuhita', 'Nyamitanga i', 'Nyamitanga ii', 'Kakamba', 'Rwenyena i', 'Rwenyena ii', 'Kabuba', 'Kasheshe', 'Kafunjo', 'Mwengura', 'Nyakatooma', 'Rwakanyonyi']),
        ('Kararo', ['Kicwamba', 'Rwemitoojo', 'Rwengyeya', 'Ryakisire', 'Karaaro', 'Kyamacumu', 'Nyariyanga', 'Kyanyamutungu', 'Kafunjo', 'Nyakayonza', 'Nkoni i', 'Nkoni ii']),
        ('Bwera', ['Bwera', 'Katookye', 'Nyambirizi', 'Nyakiborera', 'Nyakigabagaba', 'Nyakizinga']),
        ('Buyanja', ['Buyanja i', 'Buyanja ii', 'Kibingo', 'Kayanja', 'Katerero i', 'Katerero ii', 'Rwemihingo', 'Nyamitooma', 'Muraaro', 'Rukukuru']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()