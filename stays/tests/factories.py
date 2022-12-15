import factory
from stays.models import Stay, Review
from customers.tests.factories import PersonFactory, ProviderFactory


class StayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stay

    owner = factory.SubFactory(PersonFactory)
    provider = factory.SubFactory(ProviderFactory)
    start_date = '2011-01-02'
    end_date = '2011-01-03'


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    stay = factory.SubFactory(StayFactory)
    review = 'Hello world'
    rating = 4
