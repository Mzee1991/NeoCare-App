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

    # Create Subcounty/Town Council/Division - Masha
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Masha')

    # Create Parishes and Villages
    parishes = [
        ('Nyarubungo', ['Akafunda', 'Igyereka', 'Katereera', 'Rwengando', 'Ruyonza', 'Omukabare', 'Nyarubungo i', 'Nyarubungo ii']),
        ('Nyamitsindo', ['Buyojwa', 'Nyamitanga', 'Nyamitsindo', 'Kakyeka', 'Nyabushozi', 'Rwakahunde', 'Rumuri']),
        ('Rwetango', ['Rwenfunjo', 'Rwenyanga', 'Kyamuguruma', 'Rwetango a', 'Rwetango b', 'Kyarwanshashura', 'Kyekyakire', 'Nyakahita']),
        ('Rukuuba', ['Rwendezi', 'Kakuto a', 'Kakuto b', 'Rwenshebashebe', 'Nyamabare', 'Rukuuba']),
        ('Nyakakoni', ['Rwembogo', 'Masha', 'Omukabaare', 'Nyakakoni a', 'Nyakakoni b', 'Nyakakoni c', 'Nyakasharara']),
        ('Kabaare', ['Kabaare i', 'Kabaare ii', 'Kabaare iii', 'Kabaare iv', 'Kabaare v', 'Kabaare vi', 'Kabaare vii'])
    ]

    for parish_name, village_names in parishes:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        create_villages(parish, village_names)

if __name__ == '__main__':
    populate_database()