from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20, default="Cami")
    email = models.EmailField(default="cami@gmail.com")
    phone = models.PositiveIntegerField(default=893929393)
    image_url = models.ImageField(upload_to=None, default="cami.jpg")

    def __str__(self):
        return self.name


class Provider (models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)


class Pet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="Hugo")

    def __str__(self):
        return self.name
