from django.test import TestCase
from customers.models import Person
from django.core.management import call_command
from io import StringIO

class RecoveryImportTestCase(TestCase):
     def setUp(self):
      self.out = StringIO()
     
     def test_recoveryimports_run_successfully(self):
        call_command('recoveryimport',"stays/fixtures/reviews.csv", stdout=self.out)
        self.assertIn('The command has been executed successfully', self.out.getvalue())

     def test_empty_csv_file(self):
        call_command('recoveryimport',"stays/fixtures/empty.csv", stdout=self.out)
        self.assertIn('WARNING - Empty file', self.out.getvalue())

     def test_duplicate_csv_file(self):
        call_command('recoveryimport',"stays/fixtures/duplicate.csv", stdout=self.out)
        self.assertIn('The command has been executed successfully', self.out.getvalue())

     def test_missing_critical_data_file(self):
        call_command('recoveryimport',"stays/fixtures/missing_critical_data.csv", stdout=self.out)
        self.assertIn("null value", self.out.getvalue())

     def test_exceptions_file(self):
        call_command('recoveryimport',"stays/fixtures/exceptions.csv", stdout=self.out)
        self.assertIn("The imported file contains 5 errors", self.out.getvalue())

     def test_user_and_owner_file(self):
        call_command('recoveryimport',"stays/fixtures/sitter_and_owner.csv", stdout=self.out)
        self.assertIn("The command has been executed successfully", self.out.getvalue())

     def test_command_called_twice_file(self):
        call_command('recoveryimport',"stays/fixtures/reviews.csv", stdout=self.out)
        call_command('recoveryimport',"stays/fixtures/reviews.csv", stdout=self.out)
        self.assertIn("The command has been executed successfully", self.out.getvalue())
        self.assertEqual(
            Person.objects.filter(email="user3072@yahoo.com").count(), 1
        )

     def test_header_file(self):
        call_command('recoveryimport',"stays/fixtures/header.csv", stdout=self.out)
        self.assertIn("The command has been executed successfully", self.out.getvalue())
