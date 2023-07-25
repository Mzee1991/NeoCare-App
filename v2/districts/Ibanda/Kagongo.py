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

    # Create Subcounty - Kagongo division
    subcounty, _ = Subcounty.objects.get_or_create(county_municipality=county_municipality, name='Kagongo division')

    # Create Parishes and Villages

    parishes_and_villages = [
        ('Rwenshuri', ['Kabereebere', 'Byeshembe i', 'Byeshembe ii', 'Kakizerere i', 'Kakizerere ii', 'Rweshuri i', 'Rweshuri ii', 'Kashambya i', 'Rugaaga']),
        ('Nyakatokye', ['Bigyera', 'Kigaigo', 'Kigando', 'Kitooma', 'Rwebiyenje i', 'Rwebiyenje ii', 'Nyamiyaga i', 'Nyamiyaga ii', 'Ryakashoro', 'Kashaka', 'Kanama i', 'Kanama ii', 'Mishangi', 'Nyakatokye central', 'Nateete']),
        ('Kyeikucu', ['Bugorora', 'Kyarutanga i', 'Kyarutanga ii', 'Kyeikucu i', 'Kyeikucu ii', 'Mirambi', 'Mahega i', 'Mahega ii', 'Rwampanga', 'Rukokoma ii', 'Rwahura ii']),
        ('Kyaruhanga ward', ['Ibanda cell', 'Ibanda central', 'Jubilee street', 'Kitwe', 'Kyaruhanga i', 'Kyaruhanga ii', 'Kyarukobwa a', 'Kyarukobwa b', 'Kyarukoobwa b east', 'Kyarukoobwa c', 'Kyereeta', 'Main street', 'Muginda', 'Saza']),
        ('Kagongo ward', ['Buhumuriro', 'Kisiita', 'Katooma i', 'Katooma ii', 'Rwencwamba', 'Rwengiri t/centre', 'Kasharara', 'Kafunda t/centre', 'Kagongo institutions', 'Mabanga', 'Rwamukiigi', 'Rukokoma', 'Nyinendugu']),
        ('Kashangura', ['Bigyera', 'Ryakashankara', 'Kakukuru', 'Karindiriro', 'Nyamushwiga', 'Kashangura i', 'Kashangura ii', 'Kamututumi i', 'Kamututumi ii', 'Rwateibare', 'Rwahura i', 'Nyarubira']),
        ('Kanyansheko', ['Kikandure', 'Kanyansheko a', 'Kanyansheko b', 'Kabura', 'Kyarufubangi', 'Nyakigando']),
    ]

    for parish_name, village_names in parishes_and_villages:
        parish, _ = Parish.objects.get_or_create(subcounty=subcounty, name=parish_name)
        for village_name in village_names:
            village, _ = Village.objects.get_or_create(parish=parish, name=village_name)

if __name__ == '__main__':
    populate_database()