import factory
from stays.models import Stay, Review
from customers.tests.factories import PersonFactory, ProviderFactory
from datetime import date, timedelta

class StayFactory(factory.django.DjangoModelFactory):
   
    class Meta:
        model = Stay

    owner = factory.SubFactory(PersonFactory)
    provider = factory.SubFactory(ProviderFactory)
    start_date = date.today()
    end_date = date.today() + timedelta(1)


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    stay = factory.SubFactory(StayFactory)
    review = 'Hello world'
    rating = 4
