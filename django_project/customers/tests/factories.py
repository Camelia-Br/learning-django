import factory
from . import models


class PersonFactory(factory.Factory):
    class Meta:
        model = models.Person

    name = "Jhon"
    email = "Jhon@gmail.com"
    phone = 4646
    image_url = "jhon.png"


class ProviderFactory(factory.Factory):
    class Meta:
        model = models.Provider

    person = PersonFactory.create()


class PetFactory(factory.Factory):
    class Meta:
        model = models.Pet

    person = PersonFactory.create()
    name = "Loly"
