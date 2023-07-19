from django.http.response import Http404
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.views import ProviderListViewSet
from customers.models import Provider
from customers.tests.factories import ProviderFactory


class BaseAPITest(APITestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.view_set = ProviderListViewSet

    def get_request_factory(self, url, average_ratings={}, id=None):
        request = self.request_factory.get(url, average_ratings)
        return request

    def get_request_client(self, url, average_ratings={}):
        request = self.client.get(url, average_ratings)
        return request

    def get_retrieve_response(self, url, average_ratings={}, id=None):
        request = self.get_request_factory(url, average_ratings, id)
        return self.view_set.as_view({'get': 'retrieve'})(request, pk=id)

    def get_list_response(self, url, average_ratings={}, id=None):
        request = self.get_request_factory(url, average_ratings, id)
        return self.view_set.as_view({'get': 'list'})(request)


class ProviderAPITestCase(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.request_client = self.client.get
        self.url = "/api/providers/"
        self.average_ratings = {"average_rating_min": 0, "average_rating_max": 5}

    def test_retrieve_provider(self):
        self.provider = ProviderFactory.create()
        response = self.get_retrieve_response(self.url, self.average_ratings, self.provider.person.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.provider.person.name)

    def test_return_404_when_id_does_not_exists(self):
        response = self.get_retrieve_response(self.url, self.average_ratings, '0')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_list_of_providers(self):
        self.provider1 = ProviderFactory.create()
        self.provider2 = ProviderFactory.create()
        self.provider3 = ProviderFactory.create()

        response = self.get_list_response(self.url, self.average_ratings)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data[0].values())[1], self.provider1.person.name)
        self.assertEqual(len(response.data), 3)

    def test_when_min_is_greater_than_max(self):
        with self.assertRaises(ValueError) as e:
            self.get_request_client(self.url, {"average_rating_min": 5, "average_rating_max": 1})
        self.assertEqual(
            "The average_rating_min parameter should be smaller than average_rating_max",
            str(e.exception),
        )

    def test_average_rating_min_greater_than_zero_max_smaller_than_five(self):
        with self.assertRaises(ValueError) as e:
            self.get_request_client(self.url, {"average_rating_min": 0, "average_rating_max": 9})
        self.assertEqual(
            "The average_rating_min parameter should be greater than 0 and average_rating_max parameter should be smaller than 5",
            str(e.exception),
        )
