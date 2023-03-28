from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from customers.models import Provider
from customers.tests.factories import ProviderFactory
from rest_framework.test import APIClient
from api.views import ProviderListViewSet


class ProviderApiTests(APITestCase):
    def test_retrieve_provider(self):
        provider = ProviderFactory.create()
        client =APIClient()
        request = client.get('/api/provider/' + str(provider.id) + '/') 
        response = ProviderListViewSet.retrieve(self, request, pk=provider.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_one_provider(self):
        provider = ProviderFactory.create()
        client =APIClient()
        request = client.get('/api/provider/' + str(provider.id) + '/') 
        response = ProviderListViewSet.retrieve(self, request, pk=provider.id)
        self.assertEqual(response.data['name'], 'Jhon')

    def test_return_404_when_id_does_not_exists(self):
        client =APIClient()
        request = client.get('/api/provider/0/') 
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_list_of_providers(self):
        client = APIClient()
        request = client.get('/api/provider/')
        response = ProviderListViewSet.list(self, request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)