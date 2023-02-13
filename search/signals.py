from django.db.models.signals import post_save
from django.dispatch import receiver
from customers.models import Person
from .utils import recalculate_ratings_score, recalculate_sitter_score, recalculate_overall_rank

@receiver(post_save, sender=Person)
def update_search_score(sender, instance, **kwargs):
    if(hasattr(instance, 'provider')):
       recalculate_ratings_score(instance)
       recalculate_sitter_score(instance)
       recalculate_overall_rank(instance)


