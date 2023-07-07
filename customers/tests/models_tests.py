from django.core.exceptions import ValidationError
from django.test import TestCase

from customers.models import Person, Pet, Provider

from .factories import PersonFactory, PetFactory, ProviderFactory


class PersonTestCase(TestCase):
    def test_create_person(self):
        person1 = PersonFactory.create()
        self.assertIn(person1, Person.objects.all())

        try:
            person1.full_clean()
        except ValidationError as e:
            self.assertRaises('name' in e.message_dict)


class ProviderTestCase(TestCase):
    def test_provider(self):
        provider1 = ProviderFactory.create()
        self.assertIn(provider1, Provider.objects.all())

        try:
            provider1.full_clean()
        except ValidationError as e:
            self.assertRaises('name' in e.message_dict)


class PetTestCase(TestCase):
    def test_pet(self):
        pet1 = PetFactory.create()
        self.assertIn(pet1, Pet.objects.all())

        try:
            pet1.full_clean()
        except ValidationError as e:
            self.assertRaises('name' in e.message_dict)
