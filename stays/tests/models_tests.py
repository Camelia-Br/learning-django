from django.test import TestCase
from stays.models import Stay, Review
from .factories import StayFactory, ReviewFactory
from customers.tests.factories import PersonFactory, PetFactory
from django.core.exceptions import ValidationError


class StayTestCase(TestCase):
    def test_create_stay(self):
        stay = StayFactory.create()
        pet = PetFactory.create()
        stay.pets.add(pet)
        stay.save()
        stay.refresh_from_db()
        self.assertIn(stay, Stay.objects.all())
        self.assertIn(pet, stay.pets.all())

        try:
            stay.full_clean()
        except ValidationError as e:
            self.assertRaises('name' in e.message_dict)


class ReviewTestCase(TestCase):
    def test_create_review(self):
        review = ReviewFactory.create()
        self.assertIn(review, Review.objects.all())

        try:
            review.full_clean()
        except ValidationError as e:
            self.assertRaises('name' in e.message_dict)
