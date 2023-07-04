import csv
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'New Person, Provider, Pet, Stay and Review are added to database'