from dirtyfields import DirtyFieldsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .signals import person_name_changed, provider_created


class Person(DirtyFieldsMixin, models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be valid")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    image_url = models.ImageField(upload_to=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "People"


@receiver(post_save, sender=Person)
def person_name_changed_signal_handler_post_save(sender, instance, **kwargs):
    dirty_name = instance.get_dirty_fields()
    if (hasattr(instance, 'provider')) and (dirty_name and 'name' in dirty_name):
        person_name_changed.send(sender=sender, person=instance)


class Provider(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Provider for - {self.person.name} - {self.id}"

    def __repr__(self):
        return f"Provider for - {self.person.name} - {self.id}"


@receiver(post_save, sender=Provider)
def provider_created_handler_post_save(sender, instance, created, **kwargs):
    if created:
        provider_created.send(sender=sender, provider=instance)


class Pet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.person}'s pet - {self.name} - {self.id}"
