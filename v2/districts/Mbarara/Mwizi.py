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
    county_municipality, _ = CountyMunicipality.objects.get_or_create(district=district, name='Rwampara')

    # Create Subcounty
    subcounty = Subcounty.objects.create(county_municipality=county_municipality, name='Mwizi')

    # Create Parish - Bushwere
    parish1 = Parish.objects.create(subcounty=subcounty, name='Bushwere')
    village1 = Village.objects.create(parish=parish1, name='Buhungye')
    village2 = Village.objects.create(parish=parish1, name='Kabingo')
    village3 = Village.objects.create(parish=parish1, name='Kikunda i')
    village4 = Village.objects.create(parish=parish1, name='Kikunda ii')
    village5 = Village.objects.create(parish=parish1, name='Kikunda iii')
    village6 = Village.objects.create(parish=parish1, name='Kikunda iv')
    village7 = Village.objects.create(parish=parish1, name='Kitaaba')
    village8 = Village.objects.create(parish=parish1, name='Kakiiri')
    village9 = Village.objects.create(parish=parish1, name='Kyakaseeta')
    village10 = Village.objects.create(parish=parish1, name='Karuhiira')
    village11 = Village.objects.create(parish=parish1, name='Rwentojo')
    village12 = Village.objects.create(parish=parish1, name='Kasiriiri')
    village13 = Village.objects.create(parish=parish1, name='Kyonyo')
    village14 = Village.objects.create(parish=parish1, name='Ruzo')
    village15 = Village.objects.create(parish=parish1, name='Nyungu')

    # Create Parish - Kigaaga
    parish2 = Parish.objects.create(subcounty=subcounty, name='Kigaaga')
    village16 = Village.objects.create(parish=parish2, name='Ihombya')
    village17 = Village.objects.create(parish=parish2, name='Ihombya i')
    village18 = Village.objects.create(parish=parish2, name='Ihombya ii')
    village19 = Village.objects.create(parish=parish2, name='Kabatanagi')
    village20 = Village.objects.create(parish=parish2, name='Kabatanagi ii')
    village21 = Village.objects.create(parish=parish2, name='Kabaya')
    village22 = Village.objects.create(parish=parish2, name='Kikonkoma central')
    village23 = Village.objects.create(parish=parish2, name='Kikonkoma i')
    village24 = Village.objects.create(parish=parish2, name='Kikonkoma ii')
    village25 = Village.objects.create(parish=parish2, name='Kimuli')
    village26 = Village.objects.create(parish=parish2, name='Kigaaga')
    village27 = Village.objects.create(parish=parish2, name='Katookye')
    village28 = Village.objects.create(parish=parish2, name='Karamurani')
    village29 = Village.objects.create(parish=parish2, name='Rwentamu')
    village30 = Village.objects.create(parish=parish2, name='Kabura')
    village31 = Village.objects.create(parish=parish2, name='Kasharira')
    village32 = Village.objects.create(parish=parish2, name='Kyaruhenda')
    village33 = Village.objects.create(parish=parish2, name='Mwizi central')
    village34 = Village.objects.create(parish=parish2, name='Kyoma')
    village35 = Village.objects.create(parish=parish2, name='Kyoma ii')
    village36 = Village.objects.create(parish=parish2, name='Ngoma')
    village37 = Village.objects.create(parish=parish2, name='Rubagano')

    # Create Parish - Rukarabo
    parish3 = Parish.objects.create(subcounty=subcounty, name='Rukarabo')
    village38 = Village.objects.create(parish=parish3, name='Akashansha')
    village39 = Village.objects.create(parish=parish3, name='Kashojwa i')
    village40 = Village.objects.create(parish=parish3, name='Kashojwa ii')
    village41 = Village.objects.create(parish=parish3, name='Kyatoko')
    village42 = Village.objects.create(parish=parish3, name='Macuucu')
    village43 = Village.objects.create(parish=parish3, name='Marembo i')
    village44 = Village.objects.create(parish=parish3, name='Marembo ii')
    village45 = Village.objects.create(parish=parish3, name='Rukarabo')
    village46 = Village.objects.create(parish=parish3, name='Nyamabare')

    # Create Parish - Ryamiyonga
    parish4 = Parish.objects.create(subcounty=subcounty, name='Ryamiyonga')
    village47 = Village.objects.create(parish=parish4, name='Ibumba')
    village48 = Village.objects.create(parish=parish4, name='Kihangire')
    village49 = Village.objects.create(parish=parish4, name='Kakoni i')
    village50 = Village.objects.create(parish=parish4, name='Kakoni ii')
    village51 = Village.objects.create(parish=parish4, name='Rwenyaga')
    village52 = Village.objects.create(parish=parish4, name='Ryamiyonga')
    village53 = Village.objects.create(parish=parish4, name='Kyatoko')
    village54 = Village.objects.create(parish=parish4, name='Kyeyare')
    village55 = Village.objects.create(parish=parish4, name='Musheesha')

if __name__ == '__main__':
    populate_database()
