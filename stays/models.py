from django.db import models
from customers.models import Person, Provider, Pet


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


class Review(models.Model):
    stay = models.OneToOneField(Stay, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()

    def __str__(self):
        return f"Review for - {self.stay} - {self.id}"

    def __repr__(self):
        return f"Review for - {self.stay}  - {self.id}"
