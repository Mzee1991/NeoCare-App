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
    # Create District
    district, _ = District.objects.get_or_create(name='Mbarara')

    # Create County/Municipality
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Mbarara Municipality')

    # Create Subcounty - Nyakayojo
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Nyakayojo')

    # Create Parishes and Villages
    parish1 = Parish.objects.create(subcounty=subcounty, name='Bugashe ward')
    village1 = Village.objects.create(parish=parish1, name='Bugashe')
    village2 = Village.objects.create(parish=parish1, name='Kibaya i')
    village3 = Village.objects.create(parish=parish1, name='Kibaya ii')
    village4 = Village.objects.create(parish=parish1, name='Kibona')
    village5 = Village.objects.create(parish=parish1, name='Kanyamurimi')
    village6 = Village.objects.create(parish=parish1, name='Rutooma')
    village7 = Village.objects.create(parish=parish1, name='Nyakahanga')

    parish2 = Parish.objects.create(subcounty=subcounty, name='Katojo ward')
    village8 = Village.objects.create(parish=parish2, name='Kibingo')
    village9 = Village.objects.create(parish=parish2, name='Kitagata')
    village10 = Village.objects.create(parish=parish2, name='Kitooma')
    village11 = Village.objects.create(parish=parish2, name='Katojo')
    village12 = Village.objects.create(parish=parish2, name='Rwemigina')
    village13 = Village.objects.create(parish=parish2, name='Karugyembe')
    village14 = Village.objects.create(parish=parish2, name='Rwentondo')
    village15 = Village.objects.create(parish=parish2, name='Rwariire i')
    village16 = Village.objects.create(parish=parish2, name='Rwariire ii')
    village17 = Village.objects.create(parish=parish2, name='Ngaara')
    village18 = Village.objects.create(parish=parish2, name='Nyakashambya')

    parish3 = Parish.objects.create(subcounty=subcounty, name='Kichwamba ward')
    village19 = Village.objects.create(parish=parish3, name='Keishazi')
    village20 = Village.objects.create(parish=parish3, name='Kichwamba')
    village21 = Village.objects.create(parish=parish3, name='Karengye')
    village22 = Village.objects.create(parish=parish3, name='Kambaba i')
    village23 = Village.objects.create(parish=parish3, name='Kambaba ii')
    village24 = Village.objects.create(parish=parish3, name='Katanda i')
    village25 = Village.objects.create(parish=parish3, name='Katanda ii')
    village26 = Village.objects.create(parish=parish3, name='Mutukura i')
    village27 = Village.objects.create(parish=parish3, name='Mutukura ii')

    parish4 = Parish.objects.create(subcounty=subcounty, name='Nyarubungo ii ward')
    village28 = Village.objects.create(parish=parish4, name='Ibaare')
    village29 = Village.objects.create(parish=parish4, name='Kabingo')
    village30 = Village.objects.create(parish=parish4, name='Keijengye')
    village31 = Village.objects.create(parish=parish4, name='Kishenyi')
    village32 = Village.objects.create(parish=parish4, name='Kinyaza')
    village33 = Village.objects.create(parish=parish4, name='Kiboroga')
    village34 = Village.objects.create(parish=parish4, name='Katukuru')
    village35 = Village.objects.create(parish=parish4, name='Karambi')
    village36 = Village.objects.create(parish=parish4, name='Kashojwa')
    village37 = Village.objects.create(parish=parish4, name='Mabira')
    village38 = Village.objects.create(parish=parish4, name='Macuro')
    village39 = Village.objects.create(parish=parish4, name='Rwakwezi')
    village40 = Village.objects.create(parish=parish4, name='Nyamatojo')
    village41 = Village.objects.create(parish=parish4, name='Nyarubungo')

    parish5 = Parish.objects.create(subcounty=subcounty, name='Rukindo ward')
    village42 = Village.objects.create(parish=parish5, name='Bwenkoma a')
    village43 = Village.objects.create(parish=parish5, name='Bwenkoma b')
    village44 = Village.objects.create(parish=parish5, name='Nyamiyaga')
    village45 = Village.objects.create(parish=parish5, name='Kagando a')
    village46 = Village.objects.create(parish=parish5, name='Kagando b')
    village47 = Village.objects.create(parish=parish5, name='Rukindo')
    village48 = Village.objects.create(parish=parish5, name='Nyakakoni a')
    village49 = Village.objects.create(parish=parish5, name='Nyakakoni b')

    parish6 = Parish.objects.create(subcounty=subcounty, name='Rwakishakizi ward')
    village50 = Village.objects.create(parish=parish6, name='Bwigara')
    village51 = Village.objects.create(parish=parish6, name='Kibingo')
    village52 = Village.objects.create(parish=parish6, name='Kayonza')
    village53 = Village.objects.create(parish=parish6, name='Karama i')
    village54 = Village.objects.create(parish=parish6, name='Karama ii')
    village55 = Village.objects.create(parish=parish6, name='Kagasha')
    village56 = Village.objects.create(parish=parish6, name='Misyamo')
    village57 = Village.objects.create(parish=parish6, name='Rwakishakizi i')
    village58 = Village.objects.create(parish=parish6, name='Rwakishakizi ii')
    village59 = Village.objects.create(parish=parish6, name='Rucece')
    village60 = Village.objects.create(parish=parish6, name='Rucence')
    village61 = Village.objects.create(parish=parish6, name='Nshungyezi')
    village62 = Village.objects.create(parish=parish6, name='Nyakasa')

if __name__ == '__main__':
    populate_database()
