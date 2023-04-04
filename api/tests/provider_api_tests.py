from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from customers.models import Provider
from customers.tests.factories import ProviderFactory
from rest_framework.test import APIClient
from api.views import ProviderListViewSet
from django.http.response import Http404
from api.serializers import ProviderSerializer


class ProviderApiRetrieveTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_provider(self):
        provider = ProviderFactory.create()
        request = self.client.get('/api/providers/' + str(provider.id) + '/')
        response = ProviderListViewSet.retrieve(self, request, pk=provider.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], provider.person.name)

    def test_return_404_when_id_does_not_exists(self):
        request = self.client.get('/api/providers/0/')
        with self.assertRaises(Http404):
            ProviderListViewSet.retrieve(self, request, pk='0')


class ProviderApiListTests(APITestCase):
    def test_get_list_of_providers(self):
        provider1 = ProviderFactory.create()
        provider2 = ProviderFactory.create()
        provider3 = ProviderFactory.create()

        client = APIClient()
        request = client.get('/api/providers/')
        response = ProviderListViewSet.list(self, request)

        response_data_keys = []
        for key, value in response.data[0].items():
            response_data_keys += [key]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data_keys, ProviderSerializer.Meta.fields)
        self.assertEqual(len(response.data), 3)
