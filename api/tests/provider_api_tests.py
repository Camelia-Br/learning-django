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

    def get_request(self, id=None):
        request = self.request_factory.get(
            "/api/providers/", {"average_rating_min": 0, "average_rating_max": 5}
        )
        return request

    def get_retrieve_response(self, id=None):
        request = self.get_request(id)
        return self.view_set.as_view({'get': 'retrieve'})(request, pk=id)

    def get_list_response(self, id=None):
        request = self.get_request(id)
        return self.view_set.as_view({'get': 'list'})(request)


class ProviderApiRetrieveTests(BaseAPITest):
    def test_retrieve_provider(self):
        self.provider = ProviderFactory.create()
        response = self.get_retrieve_response(self.provider.person.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.provider.person.name)

    def test_return_404_when_id_does_not_exists(self):
        response = self.get_retrieve_response('0')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProviderApiListTests(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.provider1 = ProviderFactory.create()
        self.provider2 = ProviderFactory.create()
        self.provider3 = ProviderFactory.create()

    def test_get_list_of_providers(self):
        response = self.get_list_response()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data[0].values())[1], self.provider1.person.name)
        self.assertEqual(len(response.data), 3)


class ProviderFilteringTestCase(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.provider1 = ProviderFactory.create()
        self.provider2 = ProviderFactory.create()
        self.provider3 = ProviderFactory.create()

    def test_when_parameters_are_correct(self):
        request = self.request_factory.get(
            "/api/providers/", {"average_rating_min": 0, "average_rating_max": 5}
        )
        response = self.view_set.as_view({'get': 'list'})(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_when_min_is_greater_than_max(self):
        with self.assertRaises(ValueError) as e:
            self.client.get("/api/providers/", {"average_rating_min": 5, "average_rating_max": 1})
        self.assertEqual(
            "The average_rating_min parameter should be smaller than average_rating_max",
            str(e.exception),
        )

    def test_type_is_not_int(self):
        with self.assertRaises(ValueError) as e:
            self.client.get("/api/providers/", {"average_rating_min": 0, "average_rating_max": 9})
        self.assertEqual(
            "The average_rating_min parameter should begreater than 0 and average_rating_max parameter should be smaller than 5",
            str(e.exception),
        )
