from django.test import TestCase
from customers.models import Person, Provider, Pet
from .factories import PersonFactory, ProviderFactory, PetFactory


class PersonTestCase(TestCase):
    def test_create_person(self):
        person1 = PersonFactory.create()
        self.assertIn(person1, Person.objects.all())


class ProviderTestCase(TestCase):
    def test_provider(self):
        provider1 = ProviderFactory.create()
        self.assertIn(provider1, Provider.objects.all())


class PetTestCase(TestCase):
    def test_pet(self):
        pet1 = PetFactory.create()
        self.assertIn(pet1, Pet.objects.all())
