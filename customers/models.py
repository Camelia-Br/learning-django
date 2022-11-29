from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be valid")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    image_url = models.ImageField(upload_to=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Provider (models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)


class Pet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
