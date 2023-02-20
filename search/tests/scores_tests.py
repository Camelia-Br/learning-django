from django.test import TestCase
from search.models import SearchScore
from customers.tests.factories import ProviderFactory, PersonFactory
from stays.tests.factories import StayFactory, ReviewFactory
from unittest.mock import patch
from ..scoring import compute_sitter_score, compute_ratings_score


class SearchScoreTestCase(TestCase):
    def test_create_search_score_on_provider_created(self):
        provider = ProviderFactory.create()
        self.assertIn(provider.search_score, SearchScore.objects.all())

    def test_sitter_score_and_overall_rank_update_when_person_name_changes(self):
        person = PersonFactory.create()
        provider = ProviderFactory.create(person=person)
        person_name = person.name
        provider_sitter_score = provider.search_score.sitter_score
        provider_overall_rank = provider.search_score.overall_rank
        person.name = 'Mariana'
        person.save()
        person.refresh_from_db()

        self.assertNotEqual(person_name, person.name)
        self.assertNotEqual(provider_sitter_score, provider.search_score.sitter_score)
        self.assertNotEqual(provider_overall_rank, provider.search_score.overall_rank)

    def test_rating_score_is_computed_when_review_is_added(self):
        provider = ProviderFactory.create()
        stay = StayFactory.create(provider=provider)
        review = ReviewFactory.create(stay=stay)
        rating_score = compute_ratings_score(provider)
        review.save()
        review.refresh_from_db()

        self.assertEqual(rating_score, provider.search_score.rating_score)
   
 