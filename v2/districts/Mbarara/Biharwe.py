#!/usr/bin/python3

import os
import sys
import django

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from newborn.models import District, Subcounty, Parish, Village, CountyMunicipality

def populate_database():
    # Create District
    district, _ = District.objects.get_or_create(name='Mbarara')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Mbarara Municipality')

    # Create Subcounty - Biharwe
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Biharwe')

    # Create Parish - Biharwe ward
    parish1 = Parish.objects.create(subcounty=subcounty, name='Biharwe ward')
    village1 = Village.objects.create(parish=parish1, name='Biharwe central i')
    village2 = Village.objects.create(parish=parish1, name='Biharwe central ii')
    village3 = Village.objects.create(parish=parish1, name='Biharwe east')
    village4 = Village.objects.create(parish=parish1, name='Biharwe t/c')
    village5 = Village.objects.create(parish=parish1, name='Biharwe west')
    village6 = Village.objects.create(parish=parish1, name='Ekihangire')
    village7 = Village.objects.create(parish=parish1, name='Kanyara')
    village8 = Village.objects.create(parish=parish1, name='Rwemirabyo')
    village9 = Village.objects.create(parish=parish1, name='Rwenkanja')
    village10 = Village.objects.create(parish=parish1, name='Kasharara')
    village11 = Village.objects.create(parish=parish1, name='Kyanyarukondo i')
    village12 = Village.objects.create(parish=parish1, name='Kyanyarukondo ii')
    village13 = Village.objects.create(parish=parish1, name='Mailo cell')

    # Create Parish - Kishasha
    parish2 = Parish.objects.create(subcounty=subcounty, name='Kishasha')
    village14 = Village.objects.create(parish=parish2, name='Kinyaza')
    village15 = Village.objects.create(parish=parish2, name='Kibungo')
    village16 = Village.objects.create(parish=parish2, name='Rwobuyenje')
    village17 = Village.objects.create(parish=parish2, name='Rwobuyenje north')
    village18 = Village.objects.create(parish=parish2, name='Rwobuyenje south')
    village19 = Village.objects.create(parish=parish2, name='Kyempitsi')
    village20 = Village.objects.create(parish=parish2, name='Rwabukwire')
    village21 = Village.objects.create(parish=parish2, name='Nyamabare')
    village22 = Village.objects.create(parish=parish2, name='Nyakanengo')

    # Create Parish - Nyabuhama ward
    parish3 = Parish.objects.create(subcounty=subcounty, name='Nyabuhama ward')
    village23 = Village.objects.create(parish=parish3, name='Ekigando')
    village24 = Village.objects.create(parish=parish3, name='Katojo')
    village25 = Village.objects.create(parish=parish3, name='Kanyara')
    village26 = Village.objects.create(parish=parish3, name='Kakukuru')
    village27 = Village.objects.create(parish=parish3, name='Mailo-rugarama')
    village28 = Village.objects.create(parish=parish3, name='Nyaruhanga')

    # Create Parish - Nyakinengo
    parish4 = Parish.objects.create(subcounty=subcounty, name='Nyakinengo')
    village29 = Village.objects.create(parish=parish4, name='Kibwera')
    village30 = Village.objects.create(parish=parish4, name='Rwemikunyu')
    village31 = Village.objects.create(parish=parish4, name='Katamba')
    village32 = Village.objects.create(parish=parish4, name='Mwere')
    village33 = Village.objects.create(parish=parish4, name='Mukuru')
    village34 = Village.objects.create(parish=parish4, name='Migamba')
    village35 = Village.objects.create(parish=parish4, name='Rwagaju')
    village36 = Village.objects.create(parish=parish4, name='Nyakinengo')

    # Create Parish - Rwenjeru ward
    parish5 = Parish.objects.create(subcounty=subcounty, name='Rwenjeru ward')
    village37 = Village.objects.create(parish=parish5, name='Akaku')
    village38 = Village.objects.create(parish=parish5, name='Katengyeto')
    village39 = Village.objects.create(parish=parish5, name='Katerananga')
    village40 = Village.objects.create(parish=parish5, name='Rwendama')
    village41 = Village.objects.create(parish=parish5, name='Rwenjeru north')
    village42 = Village.objects.create(parish=parish5, name='Rwenjeru south')
    village43 = Village.objects.create(parish=parish5, name='Kabucebebe')
    village44 = Village.objects.create(parish=parish5, name='Kamatarisi')
    village45 = Village.objects.create(parish=parish5, name='Rwakaterera')

if __name__ == '__main__':
    populate_database()
