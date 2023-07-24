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
        village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

def create_parish_and_villages(subcounty, parish_name, village_names):
    parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
    create_villages(parish, village_names)

def populate_database():
    # Create District
    district, _ = District.objects.get_or_create(name='Kiruhura')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Kashongi')

    # Create Subcounty
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kashongi')

    # Create Parishes and Villages
    parishes_and_villages = [
        ('Rwenjubu', ['Rwenshebashebe i', 'Rwenshebashebe ii', 'Rwenshebashebe iii', 'Rwenshebashebe iv', 'Kyenshama i', 'Mushunga i', 'Mushunga ii', 'Nyakako i']),
        ('Rwanyangwe', ['Ekitokozi', 'Rwebimunyu', 'Nyamutamba', 'Kamuzinzi', 'Mabaare', 'Rwanyangwe i', 'Rwanyangwe ii', 'Rwanyangwe iii']),
        ('Ntarama', ['Akengyeya i', 'Akengyeya ii', 'Kyagwara i', 'Kyagwara ii', 'Mukiika', 'Nyabubare', 'Ntarama i', 'Ntarama ii']),
        ('Kitabo', ['Kababeizi', 'Kisha i', 'Kisha ii', 'Kitabo central', 'Kitabo i', 'Kitabo ii', 'Kitabo iv', 'Kitabo v', 'Kagando i', 'Kagando ii', 'Mbuga i', 'Mbuga ii']),
        ('Kabushwere', ['Akashenyi', 'Byembogo', 'Ekikoni', 'Rwenjubu central', 'Kabushwere i', 'Kabushwere ii', 'Kabushwere iii', 'Kyenshama ii', 'Kyenshama iii']),
        ('Kashongi', ['Kashongi central', 'Kashongi i', 'Kashongi ii', 'Mizi i', 'Mizi ii', 'Nyakako i']),
        ('Byanamira', ['Kenkyerere', 'Kenshunga', 'Kiruruma', 'Byanamira i', 'Byanamira ii', 'Ekikagate i', 'Ekikagate ii', 'Ekishunju', 'Rwozi i', 'Rwozi ii', 'Kashasha', 'Kacwagobe', 'Kyenturegye', 'Rukinga'])
    ]

    for parish_name, village_names in parishes_and_villages:
        create_parish_and_villages(subcounty, parish_name, village_names)

if __name__ == '__main__':
    populate_database()