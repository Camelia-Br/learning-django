import factory
from search.models import SearchScore
from customers.tests.factories import ProviderFactory


class SearchScoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SearchScore

    provider = factory.SubFactory(ProviderFactory)
    sitter_score = 3
    rating_score = 2
    overall_rank = 2
