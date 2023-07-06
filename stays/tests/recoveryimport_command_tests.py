from django.test import TestCase
from customers.tests.factories import PersonFactory, ProviderFactory, PetFactory
from stays.tests.factories import StayFactory
from datetime import date, timedelta
from django.core.management import call_command
from io import StringIO

class RecoveryImportTestCase(TestCase):
     def setUp(self):
        self.owner = PersonFactory.create()
        self.provider = ProviderFactory.create()
        self.pet = PetFactory.create()
        self.today = date.today()
        self.tomorrow = self.today + timedelta(1)

     def get_data(self, **kwargs):
        return {
            "owner": self.owner,
            "provider": self.provider,
            "start_date": self.today,
            "end_date": self.tomorrow,
            "pets": [self.pet],
            **kwargs,
        }

     def test_csv_file_exists(self):
        out = StringIO()
        call_command('recoveryimport', stdout=out)
        self.assertIn('Expected output', out.getvalue())
