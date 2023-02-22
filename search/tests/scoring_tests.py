from django.test import TestCase
from customers.tests.factories import ProviderFactory, PersonFactory
from unittest.mock import patch
from stays.tests.factories import StayFactory, ReviewFactory
class ScoringTestCase(TestCase):
    def setUp(self):
        self.person = PersonFactory.create()
        self.provider = ProviderFactory.create(person=self.person)
        self.stay = StayFactory.create(provider=self.provider)
    
    @patch("search.handlers.compute_sitter_score", return_value=1)
    def test_person_name_changed_handler_is_called_when_provider_is_created(self, mock_handler):
        person=PersonFactory.create(name='Linda', email='linda@gmail.com')
        provider = ProviderFactory.create(person=person)
        mock_handler.assert_called_once_with(person)

    @patch("search.handlers.compute_sitter_score", return_value=1)
    def test_person_name_changed_handler_is_called_when_name_is_updated(self, mock_handler):
        self.person.name = 'Larisa'
        self.person.save()
        self.person.refresh_from_db()
        mock_handler.assert_called_with(self.person)

    @patch("search.handlers.compute_ratings_score", return_value=1)
    def test_review_added_handler_is_called_when_review_is_created(self, mock_handler):
        review = ReviewFactory.create(stay=self.stay)
        mock_handler.assert_called_with(self.provider)

    @patch("search.handlers.compute_ratings_score", return_value=1)
    def test_review_added_handler_is_not_called_when_review_is_missing(self, mock_handler):
        mock_handler.assert_not_called()

    @patch("search.models.compute_overall_rank", return_value=3)
    def test_overall_rank_is_called(self, mock_handler):
        review = ReviewFactory.create(stay=self.stay)
        sitter_score = self.provider.search_score.sitter_score
        rating_score = self.provider.search_score.rating_score
        mock_handler.assert_called_with(self.provider, sitter_score, rating_score)

    
   