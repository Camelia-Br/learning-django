from django.db import models
from customers.models import *

class SearchScore(models.Model):
    provider = models.OneToOneField(Provider, on_delete=models.CASCADE, related_name='search_score')
    sitter_score = models.DecimalField(max_digits=2, decimal_places=1)
    rating_score = models.DecimalField(db_index=True, max_digits=2, decimal_places=1)
    overall_rank =  models.DecimalField(db_index=True, max_digits=2, decimal_places=1)
