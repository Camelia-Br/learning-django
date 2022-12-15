from django.test import TestCase
from stays.forms import StayForm, ReviewForm
from customers.tests.factories import PersonFactory, ProviderFactory, PetFactory


class StayFormTests(TestCase):
    def test_owner_is_the_same_person_as_provider(self):
        owner = PersonFactory.create()
        provider = ProviderFactory.create(person=owner)
        pet = PetFactory.create()
        data = {"owner": owner, "provider": provider, "start_date": "2022-01-01", "end_date": "2022-02-02", "pets": [pet]}
        form = StayForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['provider'], ['You cannot perform a stay for yourself'])

    def test_owner_not_the_same_person_as_provider(self):
        owner = PersonFactory.create()
        provider = ProviderFactory.create()
        pet = PetFactory.create()
        data = {"owner": owner, "provider": provider, "start_date": "2022-01-01", "end_date": "2022-02-02", "pets": [pet]}
        form = StayForm(data=data)
        self.assertTrue(form.is_valid())

    def test_start_date_greater_than_end_date(self):
        owner = PersonFactory.create()
        provider = ProviderFactory.create()
        pet = PetFactory.create()
        data = {"owner": owner, "provider": provider, "start_date": "2022-03-03", "end_date": "2022-02-02", "pets": [pet]}
        form = StayForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['end_date'], ['End date should be greater than start date.'])

    def test_end_date_greater_than_start_date(self):
        owner = PersonFactory.create()
        provider = ProviderFactory.create()
        pet = PetFactory.create()
        data = {"owner": owner, "provider": provider, "start_date": "2022-03-03", "end_date": "2022-04-04", "pets": [pet]}
        form = StayForm(data=data)
        self.assertTrue(form.is_valid())


class ReviewFormTest(TestCase):
    def test_rating_over_5(self):
        data = {"rating": "6"}
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['rating'], ['You can choose between 1 and 5'])

    def test_rating_between_1_and_5(self):
        data = {"rating": "4"}
        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())
