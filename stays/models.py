from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from customers.models import Person, Pet, Provider

from .signals import review_added


class Stay(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='stays')
    start_date = models.DateField()
    end_date = models.DateField()
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return f"Stay for - {self.owner} - {self.id}"

    def __repr__(self):
        return (
            f"Stay(id={self.id}, owner={self.owner}, provider={self.provider}, start_date={self.start_date})"
        )


class Review(DirtyFieldsMixin, models.Model):
    stay = models.OneToOneField(Stay, on_delete=models.CASCADE)
    review = models.CharField(max_length=5000)
    rating = models.IntegerField()

    def __str__(self):
        return f"Review for - {self.stay} - {self.id}"

    def __repr__(self):
        return f"Review for - {self.stay}  - {self.id}"


@receiver(post_save, sender=Review)
def review_added_post_save(sender, instance, created, **kwargs):
    review_added.send(sender=sender, provider=instance.stay.provider)
