from unittest.mock import patch

from django.test import TestCase

from customers.models import Person
from customers.tests.factories import PersonFactory, ProviderFactory
from search.models import SearchScore
from stays.tests.factories import ReviewFactory, StayFactory

from ..scoring import compute_ratings_score, compute_sitter_score


class SearchScoreTestCase(TestCase):
    def setUp(self):
        self.person = PersonFactory.create()
        self.provider = ProviderFactory.create(person=self.person)

    def test_create_search_score_on_provider_created(self):
        self.assertIn(self.provider.search_score, SearchScore.objects.all())

    def test_sitter_score_and_overall_rank_update_when_person_name_changes(self):
        person_name = self.person.name
        provider_sitter_score = self.provider.search_score.sitter_score
        provider_overall_rank = self.provider.search_score.overall_rank
        self.person.name = 'Mariana'
        self.person.save()
        self.person.refresh_from_db()
        self.assertNotEqual(person_name, self.person.name)
        self.assertNotEqual(provider_sitter_score, self.provider.search_score.sitter_score)
        self.assertNotEqual(provider_overall_rank, self.provider.search_score.overall_rank)

    def test_rating_score_is_computed_when_review_is_added(self):
        stay = StayFactory.create(provider=self.provider)
        review = ReviewFactory.create(stay=stay)
        rating_score = compute_ratings_score(self.provider)
        self.assertEqual(rating_score, self.provider.search_score.rating_score)

    def test_rating_score_is_not_computed_when_review_is_missing(self):
        stay = StayFactory.create(provider=self.provider)
        self.assertEqual(self.provider.search_score.rating_score, 0)
