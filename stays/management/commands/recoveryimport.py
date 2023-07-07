import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from customers.models import Person, Pet, Provider
from stays.models import Review, Stay


def get_or_create_pets(owner, pet_names):
    pets_list = []
    for name in pet_names.split("|"):
        pet, _ = Pet.objects.get_or_create(person=owner, name=name)
        pets_list.append(pet)
    return pets_list


def get_or_create_stays(owner, provider, start_date, end_date, pets):
    stay, _ = Stay.objects.get_or_create(
        owner=owner, provider=provider, start_date=start_date, end_date=end_date
    )
    stay.pets.add(*pets)
    return stay


class Command(BaseCommand):
    help = 'New Person, Provider, Pet, Stay and Review are added to database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        imported_rows = 0
        rows_with_errors = 0
        if not os.path.isfile(options['csv_file'][0]):
            raise CommandError(self.style.ERROR("Please enter a valid path"))

        for csv_file in options['csv_file']:
            dataReader = csv.DictReader(open(csv_file))
            for row in dataReader:
                try:
                    self.get_or_create_data(row)
                    imported_rows += 1
                except Exception as e:
                    rows_with_errors += 1
                    self.stdout.write(self.style.ERROR(e))
            if imported_rows == 0:
                self.stdout.write(self.style.WARNING("WARNING - Empty file"))
            elif rows_with_errors != 0:
                self.stdout.write(self.style.WARNING(f"The imported file contains {rows_with_errors} errors"))
        else:
            self.stdout.write(self.style.SUCCESS("The command has been executed successfully!"))

    @transaction.atomic
    def get_or_create_data(self, row):
        sitter, _ = Person.objects.get_or_create(
            email=row.get("sitter_email"),
            defaults={
                "name": row.get("sitter"),
                "phone": row.get("sitter_phone_number"),
                "image_url": row.get("sitter_image"),
            },
        )

        owner, _ = Person.objects.get_or_create(
            email=row.get("owner_email"),
            defaults={
                "name": row.get("owner"),
                "phone": row.get("owner_phone_number"),
                "image_url": row.get("owner_image"),
            },
        )

        provider, _ = Provider.objects.get_or_create(person=sitter)

        pets = get_or_create_pets(owner=owner, pet_names=row.get("dogs"))

        stays = get_or_create_stays(
            owner=owner,
            provider=provider,
            start_date=row.get("start_date"),
            end_date=row.get("start_date"),
            pets=pets,
        )

        review, _ = Review.objects.get_or_create(stay=stays, review=row.get("text"), rating=row.get("rating"))
