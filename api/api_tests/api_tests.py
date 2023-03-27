from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from customers.models import Provider
from customers.tests.factories import ProviderFactory
from rest_framework.test import APIClient
from api.views import ProviderListViewSet


class ProviderApiTests(APITestCase):
    def test_get_provider(self):
        provider = ProviderFactory.create()
        client =APIClient()
        request = client.get('/api/provider/' + str(provider.id) + '/') 
        response = ProviderListViewSet.retrieve(self, request, pk=provider.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)