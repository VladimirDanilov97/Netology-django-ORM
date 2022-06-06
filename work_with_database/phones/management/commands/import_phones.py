import csv
from django.utils.text import slugify 
from django.core.management.base import BaseCommand
from phones.models import Phone
import requests
from datetime import datetime
from django.core.files import File
from django.conf import settings

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        
        for phone in phones:      
            with open('static/img/'+phone.get('name').replace(' ', '_')+'.jpg', 'wb') as f:
                f.write(requests.get(phone.get('image')).content)
            lte_exist = lambda x: True if x == 'True' else False
        
            Phone.objects.create(
                name=phone.get('name'),
                price=int(phone.get('price')),
                image='img/'+phone.get('name').replace(' ', '_')+'.jpg',
                lte_exists=lte_exist(phone.get('lte_exists', 'False')),
                release_date=datetime.strptime(phone.get('release_date'), '%Y-%m-%d'),
                slug=slugify(phone.get('name')),
            )
