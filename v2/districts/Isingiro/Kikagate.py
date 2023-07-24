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
    # Create District - Isingiro
    district, _ = District.objects.get_or_create(name='Isingiro')

    # Create County/Municipality - Isingiro north
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Isingiro north')

    # Create Subcounty/Town Council/Division - Kikagate
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kikagate')

    # Create Parishes and Villages
    parishes = [
        ('Rwamwijuka', ['Bubaare', 'Kigando', 'Rwemizo', 'Kaburara', 'Kasharira', 'Kamwosya', 'Rwamwijuka', 'Ruyonza']),
        ('Ruyanga', ['Burambira', 'Kihande', 'Kigando', 'Katojo', 'Kasharira', 'Kyehuna', 'Ruyanga', 'Ruyonza', 'Runoni']),
        ('Nyabushenyi', ['Kiruhura', 'Nyamwerambiko', 'Kasharira', 'Kyigarama', 'Murazagye', 'Nyabushenyi cell', 'Nyabushenyi central', 'Nyarubungo']),
        ('Ntundu', ['Kagunga', 'Kabumba', 'Mbarara ii', 'Rujubuka', 'Rutare', 'Nyeihita']),
        ('Kikagate town board', ['Bwentare', 'Kikagate boarder cell', 'Kitezo', 'Rwenkuba', 'Katanga', 'Kyezimbire', 'Nyakayojo', 'Nyarubungo']),
        ('Kyezimbire', ['Keizibate', 'Kisharira', 'Enonko', 'Rwenanura', 'Kyamushaija', 'Kyempitsi', 'Rwakijuma', 'Rusharira', 'Nyakagyera']),
        ('Kamubeizi', ['Burambira', 'Kibaare', 'Kanyinya', 'Karokarungi', 'Nyamwerambiko', 'Kamubeizi', 'Katanzi', 'Mirama', 'Nyabugando', 'Rugarama', 'Nyakabungo', 'Nyakamuri']),
        ('Kajaho', ['Busheka', 'Kajaaho', 'Kajaho central', 'Rwamurunga', 'Rwangyenya', 'Rutooma', 'Rubirizi', 'Obunazi'])
    ]

    for parish_name, village_names in parishes:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()