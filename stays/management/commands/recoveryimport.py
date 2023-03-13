from django.core.management.base import BaseCommand, CommandError
from customers.models import *
from csv import DictReader

class Command(BaseCommand):
      help = 'Imports the recovered data in the review.csv file'

      def handle(self, *args, **options):
            if Person.objects.exists():
                  print('Person already exists')
                  return
            
            for row in DictReader(open('../../fixtures/person.csv')):
                  person = Person(name=row['name'], email=row['email'], phone=row['phone'], image_url=['image'])
                  person.save()
                  print('it works, this is your person:', person)


