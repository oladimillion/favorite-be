from django.conf import settings 
from django.core.management.base import BaseCommand, CommandError
from api.models import Category

import csv
import os

class Command(BaseCommand):
    help = 'Seeding category'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'api/resources/category.csv')
        with open(file_path) as f:
            data = csv.reader(f)
            for row_array in data:
                category_name = row_array[0]
                try: 
                    Category.objects.get_or_create(category_name=category_name)
                    self.stdout.write(self.style.SUCCESS(f'Successfully save "{category_name}"'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Unable to save "{category_name}"'))

