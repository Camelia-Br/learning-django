from django.dispatch import receiver

from customers.signals import person_name_changed, provider_created
from stays.signals import review_added

from .models import SearchScore
from .scoring import compute_ratings_score, compute_sitter_score


@receiver(provider_created)
def provider_created_handler(sender, provider, **kwargs):
    sitter_score = compute_sitter_score(provider.person)
    SearchScore.objects.create(provider=provider, sitter_score=sitter_score, rating_score=0)


@receiver(person_name_changed)
def person_name_changed_handler(sender, person, **kwargs):
    sitter_score = compute_sitter_score(person)
    search_score = person.provider.search_score
    search_score.sitter_score = sitter_score
    search_score.save()


@receiver(review_added)
def review_added_handler(sender, provider, **kwargs):
    rating_score = compute_ratings_score(provider)
    search_score = provider.search_score
    search_score.rating_score = rating_score
    search_score.save()
