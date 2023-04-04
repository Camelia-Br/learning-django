from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from customers.models import Provider
from customers.tests.factories import ProviderFactory
from api.views import ProviderListViewSet
from django.http.response import Http404
from django.test import RequestFactory


class BaseAPITest(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view_set = ProviderListViewSet
        self.base_url = '/api/providers/'

    def get_request_and_response(self, id=None):
        request = self.factory.get(f'{self.base_url}{id}')
        if id:
            return self.view_set.as_view({'get': 'retrieve'})(request, pk=id)
        return self.view_set.as_view({'get': 'list'})(request)


class ProviderApiRetrieveTests(BaseAPITest):
    def test_retrieve_provider(self):
        self.provider = ProviderFactory.create()
        response = self.get_request_and_response(self.provider.person.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.provider.person.name)

    def test_return_404_when_id_does_not_exists(self):
        response = self.get_request_and_response('0')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProviderApiListTests(BaseAPITest):
    def test_get_list_of_providers(self):
        self.provider1 = ProviderFactory.create()
        self.provider2 = ProviderFactory.create()
        self.provider3 = ProviderFactory.create()
        response = self.get_request_and_response()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data[0].values())[1], self.provider1.person.name)
        self.assertEqual(len(response.data), 3)
     