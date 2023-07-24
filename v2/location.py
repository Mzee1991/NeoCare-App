#!/usr/bin/python3

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from newborn.models import District, Subcounty, Parish, Village, CountyMunicipality

def populate_database():
    # Create Districts
    district1 = District.objects.create(name='Kampala')
    district2 = District.objects.create(name='Jinja')

    # Create County/Municipalities
    county_municipality1 = CountyMunicipality.objects.create(district=district1, name='Kampala Central')
    county_municipality2 = CountyMunicipality.objects.create(district=district1, name='Kawempe')
    county_municipality3 = CountyMunicipality.objects.create(district=district2, name='Jinja Municipality')
    county_municipality4 = CountyMunicipality.objects.create(district=district2, name='Jinja Division')

    # Create Subcounties
    subcounty1 = Subcounty.objects.create(county_municipality=county_municipality1, name='Makindye')
    subcounty2 = Subcounty.objects.create(county_municipality=county_municipality1, name='Nakawa')
    subcounty3 = Subcounty.objects.create(county_municipality=county_municipality2, name='Kawempe North')
    subcounty4 = Subcounty.objects.create(county_municipality=county_municipality2, name='Kawempe South')
    subcounty5 = Subcounty.objects.create(county_municipality=county_municipality3, name='Jinja East')
    subcounty6 = Subcounty.objects.create(county_municipality=county_municipality3, name='Jinja West')
    subcounty7 = Subcounty.objects.create(county_municipality=county_municipality4, name='Jinja Central')
    subcounty8 = Subcounty.objects.create(county_municipality=county_municipality4, name='Jinja South')

    # Create Parishes
    parish1 = Parish.objects.create(subcounty=subcounty1, name='Kibuye')
    parish2 = Parish.objects.create(subcounty=subcounty1, name='Lukuli')
    parish3 = Parish.objects.create(subcounty=subcounty2, name='Ntinda')
    parish4 = Parish.objects.create(subcounty=subcounty2, name='Nakawa')
    parish5 = Parish.objects.create(subcounty=subcounty3, name='Kawempe North Parish 1')
    parish6 = Parish.objects.create(subcounty=subcounty3, name='Kawempe North Parish 2')
    parish7 = Parish.objects.create(subcounty=subcounty4, name='Kawempe South Parish 1')
    parish8 = Parish.objects.create(subcounty=subcounty4, name='Kawempe South Parish 2')
    parish9 = Parish.objects.create(subcounty=subcounty5, name='Mpumudde')
    parish10 = Parish.objects.create(subcounty=subcounty5, name='Bugembe')
    parish11 = Parish.objects.create(subcounty=subcounty6, name='Jinja West Parish 1')
    parish12 = Parish.objects.create(subcounty=subcounty6, name='Jinja West Parish 2')
    parish13 = Parish.objects.create(subcounty=subcounty7, name='Jinja Central Parish 1')
    parish14 = Parish.objects.create(subcounty=subcounty7, name='Jinja Central Parish 2')
    parish15 = Parish.objects.create(subcounty=subcounty8, name='Jinja South Parish 1')
    parish16 = Parish.objects.create(subcounty=subcounty8, name='Jinja South Parish 2')

    # Create Villages
    village1 = Village.objects.create(parish=parish1, name='Kibuye Village 1')
    village2 = Village.objects.create(parish=parish1, name='Kibuye Village 2')
    village3 = Village.objects.create(parish=parish2, name='Lukuli Village 1')
    village4 = Village.objects.create(parish=parish2, name='Lukuli Village 2')
    village5 = Village.objects.create(parish=parish3, name='Ntinda Village 1')
    village6 = Village.objects.create(parish=parish3, name='Ntinda Village 2')
    village7 = Village.objects.create(parish=parish4, name='Nakawa Village 1')
    village8 = Village.objects.create(parish=parish4, name='Nakawa Village 2')
    village9 = Village.objects.create(parish=parish5, name='Kawempe North Village 1')
    village10 = Village.objects.create(parish=parish5, name='Kawempe North Village 2')
    village11 = Village.objects.create(parish=parish6, name='Kawempe North Village 3')
    village12 = Village.objects.create(parish=parish6, name='Kawempe North Village 4')
    village13 = Village.objects.create(parish=parish7, name='Kawempe South Village 1')
    village14 = Village.objects.create(parish=parish7, name='Kawempe South Village 2')
    village15 = Village.objects.create(parish=parish8, name='Kawempe South Village 3')
    village16 = Village.objects.create(parish=parish8, name='Kawempe South Village 4')
    village17 = Village.objects.create(parish=parish9, name='Mpumudde Village 1')
    village18 = Village.objects.create(parish=parish9, name='Mpumudde Village 2')
    village19 = Village.objects.create(parish=parish10, name='Bugembe Village 1')
    village20 = Village.objects.create(parish=parish10, name='Bugembe Village 2')
    village21 = Village.objects.create(parish=parish11, name='Jinja West Village 1')
    village22 = Village.objects.create(parish=parish11, name='Jinja West Village 2')
    village23 = Village.objects.create(parish=parish12, name='Jinja West Village 3')
    village24 = Village.objects.create(parish=parish12, name='Jinja West Village 4')
    village25 = Village.objects.create(parish=parish13, name='Jinja Central Village 1')
    village26 = Village.objects.create(parish=parish13, name='Jinja Central Village 2')
    village27 = Village.objects.create(parish=parish14, name='Jinja Central Village 3')
    village28 = Village.objects.create(parish=parish14, name='Jinja Central Village 4')
    village29 = Village.objects.create(parish=parish15, name='Jinja South Village 1')
    village30 = Village.objects.create(parish=parish15, name='Jinja South Village 2')
    village31 = Village.objects.create(parish=parish16, name='Jinja South Village 3')
    village32 = Village.objects.create(parish=parish16, name='Jinja South Village 4')

if __name__ == '__main__':
    populate_database()