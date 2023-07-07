from django.core.exceptions import ValidationError
from django.test import TestCase

from customers.tests.factories import PetFactory
from stays.models import Review, Stay

from .factories import ReviewFactory, StayFactory


class StayTestCase(TestCase):
    def setUp(self):
        self.stay = StayFactory.create()
        self.pet = PetFactory.create()

    def test_create_stay(self):
        self.stay.pets.add(self.pet)
        self.stay.save()
        self.stay.refresh_from_db()
        self.assertIn(self.stay, Stay.objects.all())
        self.assertIn(self.pet, self.stay.pets.all())

        try:
            self.stay.full_clean()
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
