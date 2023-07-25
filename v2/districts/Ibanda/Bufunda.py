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

    # Create Subcounty - Bufunda division
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Bufunda division')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Nyamirima', ['Kabagoma i', 'Kabagoma ii', 'Bwentaama', 'Kigyera', 'Kibaare', 'Nyamirima lower', 'Nyamirima upper', 'Rwemirabyo', 'Rwentsinga', 'Kagando', 'Mabanga', 'Ndoragi i', 'Ndoragi ii']),
        ('Rwobuzizi', ['Katembe', 'Rwobuzizi i', 'Rwobuzizi ii', 'Rwobuzizi iii', 'Kankambwe i', 'Kankambwe ii', 'Ruyomba']),
        ('Ruyonza', ['Akaibumba', 'Katete', 'Kareere i', 'Kareere ii', 'Rwamanyonyi lower', 'Nyakabungo i', 'Nyakabungo ii', 'Ruyonza middle']),
        ('Nsasi', ['Bukuto ii', 'Kibarama i', 'Kibarama ii', 'Kibirizi', 'Karushambya', 'Kyenturegye', 'Rwamanyonyi upper', 'Nsasi t/c', 'Nyakakiri']),
        ('Kikoni', ['Kikoni central', 'Kikoni east', 'Kikoni i', 'Kikoni ii', 'Rwemirama i', 'Rwemirama ii', 'Rweseta']),
        ('Kayenje', ['Kemitoojo', 'Kayenje i', 'Kayenje ii', 'Kategure', 'Kahungye', 'Nyanga', 'Rwobuhungye', 'Kyaruhimbi', 'Nyabuhikye t/c', 'Nyabwegarika', 'Ruyonza i', 'Ntungamo']),
        ('Katongore', ['Kayonza', 'Katongore i', 'Katongore ii', 'Kafunjo i', 'Kafunjo ii', 'Kafunjo iii', 'Sigirira i', 'Sigirira ii']),
        ('Bufunda ward', ['Bufunda i a', 'Bufunda i b', 'Bufunda ii', 'Bufunda street', 'Bubaare', 'Kabaruka', 'Kyabarende', 'Kyabashambo', 'Kanyinampeta', 'Kyabugaija lower', 'Kyabugaija upper', 'Kyamoshe', 'Kyegwisa', 'Kafunjo', 'Mpiira street']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()