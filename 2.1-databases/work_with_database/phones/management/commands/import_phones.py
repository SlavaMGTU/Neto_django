import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as f:
            phones = list(csv.DictReader(f, delimiter=';'))

            for phone in phones:
                # TODO: Добавьте сохранение модели
                _, phone = Phone.objects.update_or_create(
                    name=phone['name'],
                    price=phone['name'],
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                )
                print(phones)
        pass
