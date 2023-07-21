import mock
import abc

from django.test import RequestFactory
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase

from api.views import ProviderListViewSet
from customers.tests.factories import ProviderFactory


class BaseAPITest(APITestCase):
    __abstract__ = True
    
    def setUp(self):
        self.request_factory = RequestFactory()
        self.view_set = ProviderListViewSet
        self.endpoint = None

    @abc.abstractmethod
    def get_querry_params(self):
        pass

    def get_view_kwargs(self, **kwargs):
        return kwargs 

    def override_querry_params(self, querry_params):
        return mock.patch.object(self, "get_querry_params", return_value=querry_params)

    def get_base_url(self, *args, **kwargs):
        if self.endpoint is not None:
            url = reverse(
                self.endpoint,
                args=args,
                kwargs=self.get_view_kwargs(**kwargs),
            )
        else:
            raise NotImplementedError(
                "Please implement get_base_url() or define endpoint"
            )

        return url
    
    def get_url(self, *args, **kwargs):
        url = self.get_base_url(*args, **kwargs)

        querry_params = self.get_querry_params()
        if querry_params:
            url = '{}?{}'.format(url, urlencode(self.get_querry_params()))
        
        return url

    def get(self, *args, **kwargs):
        url = self.get_url(*args,**kwargs)
        return self.client.get(url)


class ProviderListAPITestCase(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.endpoint = "api:provider-list"

    def get_querry_params(self):
        return {"average_rating_min": 0, "average_rating_max": 5}

    def test_get_list_of_providers(self):
        self.provider1 = ProviderFactory.create()
        self.provider2 = ProviderFactory.create()
        self.provider3 = ProviderFactory.create()

        response = self.get()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data[0].values())[1], self.provider1.person.name)
        self.assertEqual(len(response.data), 3)

    def test_when_min_is_greater_than_max(self):
        with self.assertRaises(ValueError) as e:
            with self.override_querry_params({"average_rating_min": 5, "average_rating_max": 1}):
                self.get()
            self.assertEqual(
                "The average_rating_min parameter should be smaller than average_rating_max",
                str(e.exception),
            )

    def test_average_rating_min_greater_than_zero_max_smaller_than_five(self):
        with self.assertRaises(ValueError) as e:
            with self.override_querry_params({"average_rating_min": 0, "average_rating_max": 9}):
                self.get()
            self.assertEqual(
                "The average_rating_min parameter should be greater than 0 and average_rating_max parameter should be smaller than 5",
                str(e.exception),
            )

class ProviderDetailAPITestCase(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.endpoint = "api:provider-detail"
        self.provider = ProviderFactory.create()

    def get_view_kwargs(self, **kwargs):
        return dict({"pk":self.provider.id}, **kwargs)

    def test_provider(self):
        response = self.get()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.provider.person.name)

    def test_provider_does_not_exist(self):
        response = self.get(pk=0)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
