from django.test import TestCase
from stays.forms import StayForm, ReviewForm
from customers.tests.factories import PersonFactory, ProviderFactory, PetFactory


class StayFormTests(TestCase):
    def setUp(self):
        self.owner = PersonFactory.create()
        self.provider = ProviderFactory.create()
        self.pet = PetFactory.create()

    def get_data(self, **kwargs):
        owner = self.owner
        provider = self.provider
        pet = self.pet
        return {
            "owner": owner,
            "provider": provider,
            "start_date": "2022-01-01",
            "end_date": "2022-02-02",
            "pets": [pet],
            **kwargs,
        }

    def test_owner_is_the_same_person_as_provider(self):
        owner = self.owner
        owner_same_as_provider = ProviderFactory(person=owner)
        data = self.get_data(provider=owner_same_as_provider)
        form = StayForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["provider"], ["You cannot perform a stay for yourself"])

    def test_owner_not_the_same_person_as_provider(self):
        data = self.get_data()
        form = StayForm(data=data)
        self.assertTrue(form.is_valid())

    def test_start_date_greater_than_end_date(self):
        data = self.get_data(start_date="2022-02-02", end_date="2022-01-01")
        form = StayForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["end_date"], ["End date should be greater than start date."])

    def test_end_date_greater_than_start_date(self):
        data = self.get_data()
        form = StayForm(data=data)
        self.assertTrue(form.is_valid())


class ReviewFormTest(TestCase):
    def get_data(self, **kwargs):
        return {"review": "Hello", "rating": "4", **kwargs}

    def test_rating_over_5(self):
        data = self.get_data(rating="7")
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["rating"], ["You can choose between 1 and 5"])

    def test_rating_between_1_and_5(self):
        data = self.get_data()
        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())
