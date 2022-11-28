import factory
from customers.models import Person, Provider, Pet


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = "Jhon"
    email = "Jhon@gmail.com"
    phone = 4646
    image_url = "jhon.png"


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider

    person = factory.SubFactory(PersonFactory)


class PetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pet

    person = factory.SubFactory(PersonFactory)
    name = "Loly"
