from django.test import TestCase
from customers.tests.factories import ProviderFactory, PersonFactory
from django.contrib import admin
from customers.admin import ProviderInline, PersonAdmin, PetInline
from customers.models import Provider, Person
from django.contrib.auth.models import User
from django.test import RequestFactory

class ProviderInlineTestCase(TestCase):
    def setUp(self):
        self.provider = ProviderFactory.create()

    @classmethod
    def setUpTestData(cls):
        cls.provider_inline = ProviderInline(Provider, admin.site)
    
    def test_readonly_fields(self):
        self.assertEqual(self.provider_inline.readonly_fields, ("sitter_score", "rating_score", "overall_rank"))

    def test_provider_methods(self):
        self.assertEqual(self.provider_inline.sitter_score(self.provider), self.provider.search_score.sitter_score)
        self.assertEqual(self.provider_inline.rating_score(self.provider), self.provider.search_score.rating_score)
        self.assertEqual(self.provider_inline.overall_rank(self.provider), self.provider.search_score.overall_rank)


class PersonAdminTestCase(TestCase):
     def setUp(self):
        self.person = PersonFactory.create()
        self.inline_instances = self.person_admin.get_inline_instances(
            self.request, self.person
        )

     @classmethod
     def setUpTestData(cls):
        cls.request = RequestFactory().get("/admin")
        cls.request.user = User.objects.create_superuser(
            "admin1234", "admin@test.com", "admin1234"
        )
        cls.person_admin = PersonAdmin(Person, admin.site)


     def test_get_inline_instances_for_person_without_provider(self):
        self.assertIsInstance(self.inline_instances[0], PetInline)
     