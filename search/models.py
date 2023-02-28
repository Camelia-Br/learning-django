from django.db import models
from customers.models import Provider

from .scoring import compute_overall_rank


class SearchScore(models.Model):
    provider = models.OneToOneField(Provider, on_delete=models.CASCADE, related_name='search_score')
    sitter_score = models.DecimalField(max_digits=2, decimal_places=1)
    rating_score = models.DecimalField(db_index=True, max_digits=2, decimal_places=1)
    overall_rank = models.DecimalField(db_index=True, max_digits=2, decimal_places=1)

    def save(self, *args, **kwargs):
        self.overall_rank = compute_overall_rank(self.provider, self.sitter_score, self.rating_score)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SearchScore for - {self.provider} - {self.id}"

    def __repr__(self):
        return f"SearchScore for - {self.provider} - {self.id}"
