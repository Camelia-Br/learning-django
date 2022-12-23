from django.test import TestCase
from stays.forms import StayForm, ReviewForm
from customers.tests.factories import PersonFactory, ProviderFactory, PetFactory
from stays.tests.factories import StayFactory
from datetime import date, timedelta


class StayFormTests(TestCase):
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

    def test_owner_is_the_same_person_as_provider(self):
        owner_same_as_provider = ProviderFactory(person=self.owner)
        data = self.get_data(provider=owner_same_as_provider)
        form = StayForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["provider"], ["You cannot perform a stay for yourself"])

    def test_owner_not_the_same_person_as_provider(self):
        data = self.get_data()
        form = StayForm(data=data)
        self.assertTrue(form.is_valid())

    def test_start_date_greater_than_end_date(self):
        data = self.get_data(start_date=self.tomorrow, end_date=self.today)
        form = StayForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["end_date"], ["End date should be greater than start date."])

    def test_end_date_greater_than_start_date(self):
        data = self.get_data()
        form = StayForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_is_valid(self):
        data = self.get_data()
        form = StayForm(data=data)
        self.assertTrue(form.is_valid())
        stay = form.save()
        self.assertIsNotNone(stay)


class ReviewFormTest(TestCase):
    def setUp(self):
        self.pet = PetFactory.create()
        self.stay = StayFactory.create()
        self.stay.pets.add(self.pet)
        self.stay.save()
        self.stay.refresh_from_db()

    def get_data(self, **kwargs):
        return {"stay": self.stay, "review": "Hello", "rating": 4, **kwargs}

    def test_rating_over_5(self):
        data = self.get_data(rating=7)
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["rating"], ["You can choose between 1 and 5"])

    def test_rating_between_1_and_5(self):
        data = self.get_data()
        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_is_valid(self):
        data = self.get_data()
        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())
        stay = form.save()
        self.assertIsNotNone(stay)
